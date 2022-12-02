import os
from task2 import create_dir
import random
import shutil
import csv
from email import generator


def get_element(class_name: str) -> generator:
    for file_name in os.listdir(os.path.join("dataset", class_name)):
        yield file_name
