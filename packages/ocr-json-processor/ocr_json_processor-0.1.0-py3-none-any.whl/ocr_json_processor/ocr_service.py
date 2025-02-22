from fastapi import HTTPException
from utils import textractor_ocr_to_dict
from extractor import process_and_extract_document, clear_folder, get_sorted_data_with_page_numbers, AmazonServices
from common import create_subfolders, get_filename_without_extension
import json
import time
import os

class OCRService:
    def __init__(self):
        self.amazon_service = AmazonServices()

    def process_textractor_document(self, pdf_path):
        try:
            ocr_response = self.amazon_service.process_document(pdf_path)
            return textractor_ocr_to_dict(ocr_response)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    async def process_doc_intelligence_document(self, pdf_path, output_folder_path, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2):	
        try:
            timestamp = int(time.time())
            pdf_filename_without_extension = get_filename_without_extension(pdf_path)
            azure_ocr_json_response_path = f"azure_ocr_json_response_folder/azure_ocr_json_response_{pdf_filename_without_extension}_{timestamp}.json"
            create_subfolders(azure_ocr_json_response_path)
            pickle_file_path = f'azure_pickles/{pdf_filename_without_extension}.pickle'
            create_subfolders(pickle_file_path)
            document_dict = await process_and_extract_document(pdf_path, output_folder_path, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2)
            clear_folder(output_folder_path)
            sorted_data_with_page_numbers = get_sorted_data_with_page_numbers(
                pdf_filename_without_extension=pdf_filename_without_extension, document_dict=document_dict
            )
            ocr_response = {"azure_ocr_pages_response": {}}
            for page_num, document in sorted_data_with_page_numbers:
                ocr_response["azure_ocr_pages_response"][str(page_num)] = document.as_dict()
            with open(azure_ocr_json_response_path, "w") as file:
                file.write(json.dumps(ocr_response, indent=2))
            return ocr_response
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


# if __name__== "__main__":
#     service = OCRService()
#     response = service.process_textractor_document("files/DHOOT TRANSMISSION PRIVATE LIMITED - FINAL REPORT.pdf")
    