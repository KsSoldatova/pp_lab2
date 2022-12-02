import os
from task2 import create_dir
import random
import shutil
import csv
from email import generator


def get_element(class_name: str) -> generator:
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name


def create_randomname_file(annotation_name: str, dir_copy: str) -> None:
    file_number = list(range(10001))
    random.shuffle(file_number)
    counter = 1
    create_dir(dir_copy)