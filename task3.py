import os
from task2 import create_dir
import random
import shutil
import csv
from email import generator

def get_element(class_name:str)->generator:
    '''This function return us list of names in dataset class'''
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name
