import pytest
from ocr_json_processor.ocr_service import OCRService
import os

def test_process_textractor_document():
    service = OCRService()
    pdf_path = "path/to/sample.pdf"
    response = service.process_textractor_document(pdf_path)
    assert isinstance(response, dict)

@pytest.mark.asyncio
async def test_process_doc_intelligence_document():
    service = OCRService()
    pdf_path = "path/to/sample.pdf"
    output_folder_path = "path/to/output"
    azure_di_endpoint_1 = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT_1')
    azure_di_key_1 = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_KEY_1')
    azure_di_endpoint_2 = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_ENDPOINT_2')
    azure_di_key_2 = os.getenv('AZURE_DOCUMENT_INTELLIGENCE_KEY_2')
    response = await service.process_doc_intelligence_document(pdf_path, output_folder_path, azure_di_endpoint_1, azure_di_key_1, azure_di_endpoint_2, azure_di_key_2)
    assert isinstance(response, dict)