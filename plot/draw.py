#!/usr/bin/env python
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
from PIL import Image
import numpy as np
import os.path
from pathlib import Path

def imageplot(xmin,ymin,xmax,ymax,file_path):
	# im=np.array(Image.open('plot/apple_1.jpg'),dtype=np.uint8)
	# print(file_path)
	im=np.array(Image.open(file_path),dtype=np.uint8)
	fig,ax=plt.subplots(1)
	size=im.shape


	draw=[]

	labelsyolo=open("/home/jeffin/agrima/datasets/capgemini/dataset/labelsbbox/apple/apple_1.txt","r").read().replace("\n","").split(" ")[1:]

	labelsyolo = [float(x) for x in labelsyolo]
	print (labelsyolo)

# x=size[1]*labelsyolo[0]
# w=size[1]*labelsyolo[2]
# y=size[0]*labelsyolo[1]
# h=size[0]*labelsyolo[3]

# b1 = (2*x + w)/2
# b0 = b1 - w
# b3 = (2*y +h)/2
# b2 = b3 - h

# #(121,14,430,332)
# print (b0)
# print (b2)
# print(w,h,y)

	ax.imshow(im)
	rect=patches.Rectangle((xmin,ymin),xmax,ymax,linewidth=1,edgecolor='b',facecolor="none")
#rect=patches.Rectangle((b0,b2),w, h,linewidth=1,edgecolor='r',facecolor='none')
	ax.add_patch(rect)


	plt.show()
