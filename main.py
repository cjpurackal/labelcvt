# Author:Christie J P

import os
from converter import converter
import ensure

root_path = "/home/christie/Projects/ai/Machine_Learning/Work/agrima/dataset/test/dataset/"


def check_for_updates():
    f = open("cat.names", "r")
    category = {name.split("\n", 1)[0]: i for i, name in enumerate(f)}
    new = []
    for name in os.listdir(root_path + '/labelsxml'):
        if name not in category:
            new.append(name)
    return new


def convert(path, ifmt="xml", ofmt="yolo"):
    root_path = path

    for food_name in os.listdir(os.path.join(root_path, "labels" + ifmt)):
        converter.convert_xml_to_yolo(food_name, root_path)


def update_cat_names(root):
    f = open("cat.names", "w+")
    for cat in os.listdir(root + "/images"):
        f.write(cat + "\n")
