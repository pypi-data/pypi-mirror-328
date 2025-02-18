import json
import os

import pytest
from rara_tools.converters import SierraResponseConverter
from rara_tools.exceptions import SierraResponseConverterException

root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SIERRA_TEST_DATA_DIR = os.path.join(root, "tests", "test_data", "sierra")
INPUT_DIR = os.path.join(SIERRA_TEST_DATA_DIR, "input")
OUTPUT_DIR = os.path.join(SIERRA_TEST_DATA_DIR, "output")

example_res =  {
            "total": 100,
            "start": 50000,
            "entries": [
                {
                    "id": 1126963,
                    "updatedDate": "2016-02-09T08:42:52Z",
                    "createdDate": "2014-05-17T17:22:00Z",
                    "deleted": False,
                    "suppressed": False,
                    "marc": {
                        "leader": "00000nz  a2200145n  4500",
                        "fields": [
                            {
                                # "tag": "100",
                                "data": {
                                    "subfields": [
                                        {
                                            "code": "a",
                                            "data": "Viggor, Signe,"
                                        },
                                        {
                                            "code": "d",
                                            "data": "1975-"
                                        }
                                    ],
                                    "ind1": "1",
                                    "ind2": " "
                                }
                            },
            ]}}]}


def read_json_file(file_path):
    with open(file_path, "r") as f:
        data = f.read()
        return json.loads(data)
        
def test_convert_bibs_response():
    response = read_json_file(os.path.join(INPUT_DIR, "bibs.json"))	
        
    converter = SierraResponseConverter(response)
    data = converter.convert()
    
    expected = read_json_file(os.path.join(OUTPUT_DIR, "bibs.json"))    
    assert data == expected 
    
    
def test_convert_keywords_response():
    with open(os.path.join(INPUT_DIR, "keywords.json"), "r") as f:
        response = f.read()
        response = json.loads(response)
        
    converter = SierraResponseConverter(response)
    data = converter.convert()
    
    expected = read_json_file(os.path.join(OUTPUT_DIR, "keywords.json"))
    
    assert data == expected
    
    
def test_convert_authorities_response():
    with open(os.path.join(INPUT_DIR, "authorities.json"), "r") as f:
        response = f.read()
        response = json.loads(response)
        
    converter = SierraResponseConverter(response)
    data = converter.convert()
    
    expected = read_json_file(os.path.join(OUTPUT_DIR, "authorities.json"))
    
    assert data == expected
    
def test_convert_with_wrong_format():
    with pytest.raises(SierraResponseConverterException):
        SierraResponseConverter("$")
        
def test_convert_missing_tag():
    with pytest.raises(SierraResponseConverterException):
        response = example_res.copy()
        response["entries"][0]["marc"]["fields"][0].pop("tag", None)

        converter = SierraResponseConverter(response)
        converter.convert()
    
def test_no_entries_in_response():
    with pytest.raises(SierraResponseConverterException):
        response = example_res.copy()
        response.pop("entries", [])

        converter = SierraResponseConverter(response)
        converter.convert()
