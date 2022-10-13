# coding=utf-8
import os
import re
import json

"""
save a string variable as txt
"""
def save_as_txt(file_name, var):
    file = open("{0}.txt".format(file_name), "w")
    file.write(var)
    file.close()


"""
save directory as json
"""
def save_as_json(file_name, directory):
    with open("{0}.json".format(file_name), "w") as json_to_save:
        json.dump(directory, json_to_save, sort_keys=True, indent=4)


"""
return the first line and split sequences
"""
def seq_split(sequence_file):
    line = sequence_file.readline()
    sequence_data = sequence_file.read()
    items = re.findall(r'.{3}', sequence_data)
    return line, items


"""
read sequence file
"""


"""
read json file as dictionary
"""
def load_json(path):
    with open(path, 'rb') as json_file:
        data = json.load(json_file)
        return data


"""

"""