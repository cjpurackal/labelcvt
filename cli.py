import argparse
from converter import converter
import main
import ensure
from plot import visualize

parser = argparse.ArgumentParser(description="labelcvt cli interface")
parser.add_argument(
					"--converter",
					choices=['xml2bbox', 'bbox2yolo', 'xml2yolo'],
					help="converter options"
					)
parser.add_argument(
					"--visualize",
					choices=['xml', 'bbox', 'yolo', 'json'],
					help="visualize options"
					)
parser.add_argument("--dataset_path", help="source label path")
parser.add_argument("--cat_names", help="category names")
args = parser.parse_args()

def label_converter(conv_type):
	cat_names = args.cat_names

	if conv_type == "xml2bbox":
		lfmt = "xml"
		ifmt = "jpg"
		res = ensure.ensure(args.dataset_path, ifmt, lfmt)
		if res == "OK":
			print("Everything loooks good!")
			main.convert(
						args.dataset_path,
						converter.convert_xml_to_bbox,
						cat_names,
						"xml",
						"txt"
						)
		else:
			print ("not ok :(")
			print (res)

	elif conv_type == "bbox2yolo":
		lfmt = "bbox"
		ifmt = "jpg"
		res = ensure.ensure(args.dataset_path, ifmt, lfmt)
		if res == "OK":
			print("Everything loooks good!")
			main.convert(
						args.dataset_path,
						converter.convert_bbox_to_yolo,
						cat_names,
						"bbox",
						"txt"
						)
		else:
			print ("not ok :(")
			print (res)
	elif conv_type == "xml2yolo":
		lfmt = "xml"
		ifmt = "jpg"
		res = ensure.ensure(args.dataset_path, ifmt, lfmt)
		if res == "OK":
			print("Everything loooks good!")
			main.convert(
						args.dataset_path,
						converter.convert_xml_to_yolo,
						cat_names,
						"xml",
						"txt"
						)
		else:
			print ("not ok :(")
			print (res)

def visualizer(visualize_type):
	if visualize_type=="xml":
		visualize.visualizexml(args.dataset_path,args.cat_names)
	elif visualize_type=="yolo":
		visualize.visualizeyolo(args.dataset_path,args.cat_names)
	elif visualize_type=="bbox":
		visualize.visualizebbox(args.dataset_path,args.cat_names)
	elif visualize_type=="json":
		visualize.visualizejson(args.dataset_path,args.cat_names)
	#args.dataset_path will retrun dataset path
	#args.cat_names refers to file containign required categories


if __name__ == "__main__":
	conv_type = args.converter
	visualize_type = args.visualize
	if visualize_type is not None:
		visualizer(visualize_type)
	elif conv_type is not None:
		label_converter(conv_type)
