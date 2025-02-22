import pytest
from ocr_json_processor.utils import convert_polygon_list, transform_leaf_nodes, check_value_type

def test_convert_polygon_list():
    polygon = [0, 0, 1, 1, 2, 2, 3, 3]
    expected_output = [
        {"x": 0.0, "y": 0.0},
        {"x": 1.0, "y": 1.0},
        {"x": 2.0, "y": 2.0},
        {"x": 3.0, "y": 3.0}
    ]
    assert convert_polygon_list(polygon) == expected_output

def test_transform_leaf_nodes():
    data = {
        "cash": [
            [
                "1120 - Operating Trust Account",
                "-4960.59",
                3
            ]
        ]
    }
    expected_output = {
        "cash": [
            {
                "1120 - Operating Trust Account": {
                    "value": "-4960.59",
                    "page_number": 3
                }
            }
        ]
    }
    assert transform_leaf_nodes(data) == expected_output

def test_check_value_type():
    assert check_value_type("123.45") == True
    assert check_value_type("123") == True
    assert check_value_type("123.456") == False
    assert check_value_type("abc") == False