from ocr_json_processor.main import JSONUpdater
import json
from openai_test_json import orix_resp, tvs_resp, essent_resp

with open('ocr_json_response.json') as file:
    ocr_response = json.load(file)

ocr_response_type = 'doc_intelligence'
with open('openai_json_response.json') as f:
    openai_json_response = json.load(f)

# openai_json_response = essent_resp

json_updater = JSONUpdater()
result = json_updater.update_confidence_score_with_coordinates(openai_json_response, ocr_response, ocr_response_type)
print(result)