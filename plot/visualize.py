import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os
import sys
import numpy as np
from PIL import Image
import xml.etree.ElementTree as et

def visualize(dataset_dir,file_path):
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
						