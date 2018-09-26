import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys
import numpy as np
from PIL import Image
import xml.etree.ElementTree as et

def visualizeyolo(dataset_dir,file_path):
	cat_name=open(file_path,"r")
	cat_name=cat_name.readlines()
	for i,p in enumerate(cat_name):
		cat_name[i]=p.split("\n")[0]
	for i in os.listdir(os.path.join(dataset_dir,"labelsyolo")):
		if i in cat_name:
			for cats in os.listdir(os.path.join(dataset_dir,"labelsyolo",i)):
				image_name=cats.split(".")[0]+".jpg"
				lines=open(os.path.join(dataset_dir,"labelsyolo",i,cats),"r")
				line=lines.readlines()
				xmin=[]
				ymin=[]
				width=[]
				height=[]
				image=os.path.join(dataset_dir,"images",i,image_name)
				w_,h_=Image.open(image).size
				for data in line:
					x_norm=float(data.split(" ")[1])
					y_norm=float(data.split(" ")[2])
					w_norm=float(data.split(" ")[3])
					h_norm=float(data.split(" ")[4])
					xmid=x_norm*w_
					ymid=y_norm*h_
					w=w_norm*w_
					h=h_norm*h_
					x1=xmid-w/2
					y1=ymid-h/2
					xmin.append(x1)
					ymin.append(y1)
					width.append(w)
					height.append(h)
				fig,ax=plt.subplots(1)
				im=np.array(Image.open(image),dtype=np.uint8)
				ax.imshow(im)
				print(xmin)
				for o in range(len(xmin)):
					s=patches.Rectangle((xmin[o],ymin[o]),width[o],height[o],linewidth=1,edgecolor='b',facecolor="none")
					ax.add_patch(s)
				plt.show()

def visualizebbox(dataset_dir,file_path):
	cat_name=open(file_path,"r")
	cat_name=cat_name.readlines()
	for i,p in enumerate(cat_name):
		cat_name[i]=p.split("\n")[0]
	for i in os.listdir(os.path.join(dataset_dir,"labelsbbox")):
		if i in cat_name:
			for cats in os.listdir(os.path.join(dataset_dir,"labelsbbox",i)):
				image_name=cats.split(".")[0]+".jpg"
				lines=open(os.path.join(dataset_dir,"labelsbbox",i,cats),"r")
				line=lines.readlines()
				xmin=[]
				ymin=[]
				width=[]
				height=[]
				image=os.path.join(dataset_dir,"images",i,image_name)
				w_,h_=Image.open(image).size
				for datas in line:
					if len(datas)==2:
						pass
					else:
						xmin.append(int(datas.split(" ")[0]))
						ymin.append(int(datas.split(" ")[1]))
						width.append(int(datas.split(" ")[2]) - int(datas.split(" ")[0]))
						height.append(int(datas.split(" ")[3].split("\n")[0]) - int(datas.split(" ")[1]))
				fig,ax=plt.subplots(1)
				im=np.array(Image.open(image),dtype=np.uint8)
				ax.imshow(im)
				for o in range(len(xmin)):
					s=patches.Rectangle((xmin[o],ymin[o]),width[o],height[o],linewidth=1,edgecolor='b',facecolor="none")
					ax.add_patch(s)
				plt.show()




def visualizexml(dataset_dir,file_path):
	# dataset_dir=sys.argv[1:][0]
	# file_path='/home/jeffin/Documents/cat.names'
	cat_name=open(file_path,"r")
	cat_name=cat_name.readlines()
	for i,p in enumerate(cat_name):
		cat_name[i]=p.split("\n")[0]
	for i in os.listdir(dataset_dir):
		if i =="labelsxml":
			for j in os.listdir(os.path.join(dataset_dir,"labelsxml")):
				if j in cat_name:
					for cats in os.listdir(os.path.join(dataset_dir,"labelsxml",j)):
						image_name=cats.split(".")[0]+".jpg"
						tree=et.parse(os.path.join(dataset_dir,"labelsxml",j, cats))
						root=tree.getroot()
						k=root.findall('object')
						xmax=[]
						ymax=[]
						xmin=[]
						ymin=[]
						for group in root.findall('object'):
							title=group.find('bndbox')
							xmax.append(int(title.find('xmax').text))
							xmin.append(int(title.find('xmin').text))
							ymax.append(int(title.find('ymax').text))
							ymin.append(int(title.find('ymin').text))
						image=os.path.join(dataset_dir,"images",j,image_name)
						print (image)
						fig,ax=plt.subplots(1)
						im=np.array(Image.open(image),dtype=np.uint8)
						ax.imshow(im)
						print(xmin)
						for i in range(len(xmin)):
							s=patches.Rectangle((xmin[i],ymin[i]),xmax[i]-xmin[i],ymax[i]-ymin[i],linewidth=1,edgecolor='b',facecolor="none")
							ax.add_patch(s)
						plt.show()
						