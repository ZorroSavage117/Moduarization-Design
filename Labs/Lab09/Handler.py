import json
import os

def get_filename():
    while True:
        print("Open a file of unsorted list? (ends in .json)")
        filename = input("> ")
        try:
            with open(filename, "r") as f:
                return filename  # If the file exists, return its name
        except FileNotFoundError:
            print("File does not exist. Please check spelling.")
        print(f"Debug: file variable contains '{filename}'")

def load_file(filename):
    with open(filename, "r") as file_data:
        data = json.load(file_data)
    list_num = input("Which list do you want to sort? (1/2/3)\n> ")
    unsorted_list = data.get(list_num)
    return unsorted_list

def load_test_lists():
    with open("test_lists.json", "r") as file_data:
        data = json.load(file_data)
    unsorted_list_dic = data.get("test_cases")
    return unsorted_list_dic

script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)