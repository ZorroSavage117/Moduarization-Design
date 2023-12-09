import json
import os

def load_test_lists():
    with open("test_lists.json", "r") as file_data:
        data = json.load(file_data)
    unsorted_list_dic = data.get("test_cases")
    return unsorted_list_dic

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)