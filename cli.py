import argparse
from converter import converter
import main
import ensure

parser = argparse.ArgumentParser(description="labelcvt cli interface")
parser.add_argument(
					"converter",
					choices=['xml2bbox', 'bbox2yolo', 'xml2yolo'],
					help="converter options"
					)
parser.add_argument("--label_path", help="source label path")
parser.add_argument("--cat_names", help="category names")
args = parser.parse_args()
conv_type = args.converter
cat_names = args.cat_names

if conv_type == "xml2bbox":
	lfmt = "xml"
	ifmt = "jpg"
	res = ensure.ensure(args.label_path, ifmt, lfmt)
	if res == "OK":
		print("Everything loooks good!")
		main.convert(
					args.label_path,
					converter.convert_xml_to_bbox,
					cat_names,
					"xml",
					"txt"
					)
	else:
		print ("not ok :(")
		print (res)

elif conv_type == "bbox2yolo":
	lfmt = "txt"
	ifmt = "jpg"
	res = ensure.ensure(args.label_path, ifmt, lfmt)
	if res == "OK":
		print("Everything loooks good!")
		main.convert(
					args.label_path,
					converter.convert_bbox_to_yolo,
					cat_names,
					"txt",
					"txt"
					)
	else:
		print ("not ok :(")
		print (res)
elif conv_type == "xml2yolo":
	lfmt = "xml"
	ifmt = "jpg"
	res = ensure.ensure(args.label_path, ifmt, lfmt)
	if res == "OK":
		print("Everything loooks good!")
		main.convert(
					args.label_path,
					converter.convert_xml_to_yolo,
					cat_names,
					"xml",
					"txt"
					)
	else:
		print ("not ok :(")
		print (res)
