#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
filename = "add_item.json"
try:
    last_list = load_from_json_file(filename)
except FileNotFoundError:
    last_list = []
for count, item in sys.argv[1]:
    last_list.append(item)
save_to_json_file(last_list, filename)
