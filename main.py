#Author:Christie J P

import os
from converter import converter
import ensure

root_path = "/home/christie/Projects/ai/Machine_Learning/Work/agrima/dataset/test/dataset/"

with open("cat.names", "r") as f:
	category = {name.split("\n",1)[0]:i for i,name in enumerate(f)}



def check_for_updates():
	new = []
	for name in os.listdir(root_path+'/labelsxml'):
		if name not in category:
			new.append(name)
	return new



def convert(path, ifmt="xml", ofmt="yolo"):
	root_path = path

	for food_name in os.listdir(os.path.join(root_path,"labels"+ifmt)):
		converter.convert_xml_to_yolo(food_name, root_path)














