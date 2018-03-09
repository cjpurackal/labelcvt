# this file deals with ensure function 
import os


def ensure(root, ifmt, lfmt):
	res = directory_structure(root)
	if res == -1:
		return "Invalid directory structure at {}".format(root)
	res = folder_names(root, lfmt)
	if res != "OK":
		return "Folder name mismatch!  {}".format(res)
	res = file_names(root, lfmt)
	if res != "OK":
		return "File name mismatch! {}".format(res)
	res = store(root, lfmt)	
	if res != "OK":
		return "File name redundancy! {}".format(res)
	res = file_format(root, ifmt, lfmt)
	if res != "OK":
		return "File format error! {}".format(res)

	res = label_img_count(root, lfmt)
	if res == -1:
		return "Label and Image count mismatch! {}".format(res)
	return "OK"

def directory_structure(root):
	req_dirs = ['images','labelsxml','lablestxt','labelsyolo', 'labelsbbox', 'unlabelled', 'lost']
	dirs = os.listdir(root)
	if not set(dirs).issubset(req_dirs):
		return -1
	else:
		return 0


def folder_names(root, lfmt):
	for img_fol,lab_fol in zip(sorted(os.listdir(root+"/images")), sorted(os.listdir(root+"/labels{}".format(lfmt)))):
		#assert img_fol == lab_fol, img_fol+" and " + lab_fol + " doesn't match!"
		if img_fol != lab_fol:
			return img_fol + " and " + lab_fol + " doesn't match!"

	return "OK"

def file_names(root, lfmt):

	for img_fol,lab_fol in zip(os.listdir(root+"/images"), os.listdir(root+"/labels{}".format(lfmt))):
		for img_file,lab_file in zip(sorted(os.listdir(root+"/images/"+img_fol)), sorted(os.listdir(root+"/labels{}/".format(lfmt)+lab_fol))):
				if img_file[:-4] != lab_file[:-4]:
					return img_fol + "/" + img_file + " and " + lab_fol + "/" + lab_file + " doesn't match!"


	return "OK" 

def store(root, lfmt):
	img_names = {}
	lab_names = {}
	for img_fol,lab_fol in zip(os.listdir(root+"/images"), os.listdir(root+"/labels{}".format(lfmt))):
		for img_file,lab_file in zip(sorted(os.listdir(root+"/images/"+img_fol)), sorted(os.listdir(root+"/labels{}/".format(lfmt)+lab_fol))):

			if img_file not in img_names:
				img_names[img_file] = img_fol
			else:
				return img_names[img_file] + "/" + img_file + " and " + img_fol + "/" + img_file + " matches! (SAME FILE NAME)!"

			if lab_file not in lab_names:
				lab_names[lab_file] = lab_fol
			else:
				return lab_names[lab_file] + "/" + lab_file + " and " + lab_fol + "/" + lab_file + " matches! (SAME FILE NAME)!"
	return "OK"			


def file_format(root, ifmt, lfmt):
	for img_fol,lab_fol in zip(os.listdir(root+"/images"), os.listdir(root+"/labels{}".format(lfmt))):
		for img_file,lab_file in zip(sorted(os.listdir(root+"/images/"+img_fol)), sorted(os.listdir(root+"/labels{}/".format(lfmt)+lab_fol))):
			if img_file.count(ifmt) > 1:
				return img_fol + "/" + img_file + " has incorrect file format!"
			if lab_file.count(lfmt) > 1:
				return lab_fol + "/" + lab_file + " has incorrect file format!"

	return "OK"




def label_img_count(root, lfmt):
	img_count = len(os.listdir(os.path.join(root, "images")))
	lbl_xml_count = len(os.listdir(os.path.join(root, "labels{}".format(lfmt))))
	if img_count != lbl_xml_count:
		return -1
	return 0



