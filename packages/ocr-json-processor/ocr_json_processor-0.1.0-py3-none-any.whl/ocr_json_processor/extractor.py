import logging
import random
import sys
import pickle
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
from PIL import Image
import subprocess
import asyncio
import shutil
import os
import platform
from textractor import Textractor
from textractor.data.constants import TextractFeatures
import fitz
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import ContentFormat
from utils import clear_folder, pdf_to_images, tif_to_jpeg, convert_to_jpeg, process_image

load_dotenv()

MAX_RETRY_COUNT = 2
RETRY_DELAY = 5
GS_PATH = 'gs'

logger = logging.getLogger('orix-poc-logger')

if platform.system() == 'Windows':
    GS_PATH = r"C:\Program Files\gs\gs10.03.1\bin\gswin64c.exe"

class AmazonServices:
    def __init__(self):
        AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
        region_name = os.getenv('AWS_REGION')

        # Initialize Textractor
        self.textractor = Textractor()


    def process_document(self, pdf_path):
        # Example processing function
        document_dict = {}
        for page_number, page in enumerate(self._get_pages_from_pdf(pdf_path)):
            pix = page.get_pixmap()
            image_path = f"temp_page_{page_number}.png"
            pix.save(image_path)
            
            # Process each page with Textractor
            textract_features = [
                TextractFeatures.FORMS,
                TextractFeatures.TABLES,
                TextractFeatures.LAYOUT
            ]
            
            # Extract text and layout information
            document = self.textractor.analyze_document(
                file_source=image_path,
                features=textract_features
            )
            
            # Get structured content
            document_dict[page_number] = document.pages[0]
        return document_dict
            
    def _get_pages_from_pdf(self, pdf_path):
        # Open the PDF file
        pdf_document = fitz.open(pdf_path)
        return pdf_document




async def analyze_document_async(document_analysis_client, image, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2):
    loop = asyncio.get_event_loop()
    # Use run_in_executor to load workbook asynchronously
    # await asyncio.sleep(5)

    def wrapper():
        logger.info("*" * 10)

        rand_int = random.randint(1, 1000)

        endpoint = azure_di_endpoint_1
        key = azure_di_key_1

        if rand_int % 2 == 0:
            endpoint = azure_di_endpoint_2
            key = azure_di_key_2

        document_intelligence_client = DocumentIntelligenceClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(key)
        )



        # Analyze the document
        poller = document_intelligence_client.begin_analyze_document(
            "prebuilt-layout", analyze_request=image, content_type="application/octet-stream", output_content_format=ContentFormat.MARKDOWN
        )
        
        result = poller.result()
        return result

    document = await loop.run_in_executor(None, wrapper)
    return document


async def extract_document_data(semaphore, document_analysis_client, image_path, page_num, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2):
    async with semaphore:
        for retry_count in range(MAX_RETRY_COUNT + 1):
            try:
                # image = Image.open(image_path)
                image_data = None
                if retry_count > 0:
                    logger.info(f'\n\nTrying again, retry_count: {retry_count + 1}, Extracting text: Page {page_num}')
                else:
                    logger.info(f'Extracting text: Page {page_num}')
                with open(image_path, "rb") as image_file:
                    # image_data = f.read()
                    document = await analyze_document_async(document_analysis_client, image_file, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2)
                return page_num, document
            except Exception as e:
                logger.info(
                    f"Exception Occurred in extracting data from {image_path}: {e}")
                logger.info(f"image {image_path} size: {Image.open(image_path).size}\n\n")

                # logger.info("\n\n\tDocument extraction interrupted, Please resolve above error.\n\n")

                if retry_count == MAX_RETRY_COUNT:
                    logger.info(f'\n\nMAX_RETRY_COUNT={MAX_RETRY_COUNT} exceeded, please process the document again.\n\n')
                    sys.exit()
                else:              
                    await asyncio.sleep(RETRY_DELAY)
                


async def extract_data_from_folder(folder_path, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2):
    results_dict = {}
    try:
        document_analysis_client = None
        # extractor = Textractor(region_name=region_name)
    except Exception as e:
        logger.error(f"Exception while initializing OCR service: {e}")
    else:
        semaphore = asyncio.BoundedSemaphore(5)
        tasks = [
            extract_document_data(
                semaphore,
                document_analysis_client,
                os.path.join(folder_path, file_name),
                os.path.splitext(file_name)[0],
                azure_di_endpoint_1,
                azure_di_key_1,
                azure_di_endpoint_2,
                azure_di_key_2
            )
            for file_name in os.listdir(folder_path)
            if file_name.endswith((".png", ".jpeg"))
        ]
        for res in asyncio.as_completed(tasks):
            page_num, document = await res
            if document:
                results_dict[page_num] = document

    return results_dict


async def process_and_extract_document(input_file_path, folder_path, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2):
    file_name, file_extension = os.path.splitext(
        os.path.basename(input_file_path))
    output_folder_path = os.path.join(folder_path, file_name)
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    images_folder = os.path.join(output_folder_path, "images")
    processed_images_folder = os.path.join(
        output_folder_path, "processed_images")
    excel_folder = os.path.join(output_folder_path, "excel")
    final_excel_folder = os.path.join(output_folder_path, "Final_Output")
    input_text_folder = os.path.join(output_folder_path, "input_text")

    for folder in [images_folder, processed_images_folder, excel_folder, final_excel_folder, input_text_folder]:
        if os.path.exists(folder):
            clear_folder(folder)
        else:
            os.makedirs(folder)

    if file_extension.lower() == '.pdf':
        pdf_to_images(input_file_path, images_folder)
    elif file_extension.lower() in (".tif", ".tiff"):
        tif_to_jpeg(input_file_path, images_folder)
    elif file_extension.lower() in (".png", ".jpeg", ".jpg"):
        convert_to_jpeg(input_file_path, images_folder)

    page_num = 1

    while True:
        image_path = os.path.join(
            images_folder, f"output_page-{page_num}.jpeg")

        if not os.path.exists(image_path):
            break

        process_image(image_path, output_folder_path)
        page_num += 1

    document_dict = await extract_data_from_folder(processed_images_folder, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2)
    return document_dict


def sort_and_extract_page_numbers(data_dict):
    # Function to extract the page number from the key
    def page_number(key):
        return int(key.split("-")[1])

    # Sorting the dictionary by the extracted page number and creating a list of tuples (page_number, data)
    sorted_data = [
        (page_number(key), value)
        for key, value in sorted(
            data_dict.items(), key=lambda item: page_number(item[0])
        )
    ]
    return sorted_data


def get_sorted_data_with_page_numbers(pdf_filename_without_extension, document_dict):
    if not os.path.exists(f'azure_pickles/{pdf_filename_without_extension}.pickle'):
        sorted_data_with_page_numbers = sort_and_extract_page_numbers(
            document_dict)
        with open(f'azure_pickles/{pdf_filename_without_extension}.pickle', 'wb') as pickle_file:
            pickle.dump(sorted_data_with_page_numbers, pickle_file,
                        protocol=pickle.HIGHEST_PROTOCOL)

    with open(f'azure_pickles/{pdf_filename_without_extension}.pickle', 'rb') as pickle_file:
        return pickle.load(pickle_file)

