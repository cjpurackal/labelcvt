#Author:Christie J P

import sys
import os
from os import listdir, getcwd, walk
from lxml import etree
from PIL import Image
import converter.utils as utils

with open("cat.names", "r") as f:
	category = {name.split("\n",1)[0]:i for i,name in enumerate(f)}



def convert_xml_to_bbox(food_name, root_path):	

	f = open("cat.names", "r")
	category = {name.split("\n",1)[0]:i for i,name in enumerate(f)}
	wd = getcwd()
	#if not exits, create the results folder 
	if not os.path.exists(root_path+'/labelsbbox/'):
		os.mkdir(root_path+'/labelsbbox/')
	
	if not os.path.exists(root_path+'/labelsbbox/'+food_name):
		os.mkdir(root_path+'/labelsbbox/'+food_name)
	k=1
	for dirName, subdirList, nameFile in os.walk(root_path + "/labelsxml/" + food_name):
		
		for nameF in nameFile:
			
			print("processing {}".format(nameF))
			
			nameF=nameF.replace('.xml','')
			
			doc = etree.parse(root_path + "/labelsxml/" + food_name + "/" + nameF+'.xml')
			raiz=doc.getroot()
			labelbbox=open('%s/labelsbbox/%s/%s.txt'%(root_path, food_name, nameF),'w')
			labelbbox.write( '%d'%(category[food_name]))
			labelbbox.write('\n')
			
			for n in range(len(raiz)):
				
				if raiz[n].tag == 'object':
			
					name = raiz[n].find('name').text
									
					if raiz[n].find('truncated')==None:
						truncated =float(0)
					else:
						truncated = float(raiz[n].find('truncated').text)
					
					bbox_xmin = float(raiz[n].find('bndbox/xmin').text)				
					bbox_ymin = float(raiz[n].find('bndbox/ymin').text)
					bbox_xmax = float(raiz[n].find('bndbox/xmax').text)
					bbox_ymax = float(raiz[n].find('bndbox/ymax').text)

					labelbbox.write('%d'%(bbox_xmin))
					labelbbox.write(' ')
					labelbbox.write('%d'%(bbox_ymin))
					labelbbox.write(' ')
					labelbbox.write('%d'%(bbox_xmax))
					labelbbox.write(' ')
					labelbbox.write('%d'%(bbox_ymax))
					labelbbox.write('\n')
			
			labelbbox.close()



def convert_bbox_to_yolo(food_name, root_path):
	
	f = open("cat.names", "r")
	category = {name.split("\n",1)[0]:i for i,name in enumerate(f)}


	cls_id = category[food_name]
	outpath = os.path.join(root_path,"labelsyolo",food_name)

	if not os.path.exists(root_path+'/labelsyolo/'):
		os.mkdir(root_path+'/labelsyolo/')
	
	if not os.path.exists(root_path+'/labelsyolo/'+food_name):
		os.mkdir(root_path+'/labelsyolo/'+food_name)

	wd = getcwd()	
	txt_name_list = []
	for (dirpath, dirnames, filenames) in walk(os.path.join(root_path,"labelsbbox",food_name)):
		txt_name_list.extend(filenames)
		break		

	for txt_name in txt_name_list:
		txt_path = os.path.join(root_path,"labelsbbox",food_name,txt_name)
		txt_file = open(txt_path, "r")
		lines = txt_file.read().split('\n')   #for ubuntu, use "\r\n" instead of "\n"
		
		txt_outpath = os.path.join(outpath,txt_name)
		txt_outfile = open(txt_outpath, "w")
		
		
		""" Convert the data to YOLO format """
		ct = 0
		for line in lines:
			if(len(line) >= 4):
				ct = ct + 1
				#print(line + "\n")
				elems = line.split(' ')
				#print(elems)
				xmin = elems[0]
				xmax = elems[2]
				ymin = elems[1]
				ymax = elems[3]
				img_path = str('%s/%s.jpg'%(os.path.join(root_path, "images", food_name), os.path.splitext(txt_name)[0]))
				im=Image.open(img_path)
				w= int(im.size[0])
				h= int(im.size[1])
				b = (float(xmin), float(xmax), float(ymin), float(ymax))
				bb = utils.convert((w,h), b)
				txt_outfile.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')



def convert_xml_to_yolo(food_name, root_path):

	convert_xml_to_bbox(food_name, root_path)
	convert_bbox_to_yolo(food_name, root_path)









#convert_xml_to_bbox("amaranth", "/home/christie/Projects/ai/Machine_Learning/Work/agrima/dataset/test/dataset/")
#convert_bbox_to_yolo("amaranth", "/home/christie/Projects/ai/Machine_Learning/Work/agrima/dataset/test/dataset/")

