from task1 import run1
from task2 import run2
from task3 import run3
from task4 import get_next_element

if __name__ == '__main__':
    run1('rose', 'annotation1.csv')
    run2('dataset_copy_1', 'annotation.csv')
    run3('annotation.csv', 'dataset_copy_2')
    for element in get_next_element("rose"):
        print(element)
    for element in get_next_element("tulip"):
        print(element)
