
from pathlib import Path
import os.path
import shutil
import imghdr
import time
from tkinter import *
import ensure
import preprocess as p
from shutil import copy2
import os

	#compare function
def filestosend(self):
	print("Ready to compare files")
	i=0;
	datalist=[]
		#os.path.join('/home/caroline/Desktop/data',x)
		#print(os.listdir(folder))
	f=open('/home/caroline/Desktop/data/data.txt',"w+")
	for x in os.listdir('/home/caroline/Desktop/data'):
		if (imghdr.what(os.path.join('/home/caroline/Desktop/data',x)) =="jpeg"):
			f.write(x+"\n")
	f.close()
		#server data
	r=open('/home/caroline/Desktop/data/data.txt','r+')

	fl=r.readlines()
	k=0
		#new upload
	c=open('/home/caroline/Desktop/data/newdata.txt',"w+")
	print(self.directory)
	for img in os.listdir(os.path.join(self.directory,'temp')):
		c.write(img+"\n")
	c.close()
	p=open('/home/caroline/Desktop/data/newdata.txt',"r+")
	send=open('/home/caroline/Desktop/data/senddata.txt',"w+")
	fn=p.readlines()
	for j in fn:
		k=0
		for i in fl:
			if(i==j):
				k=1
		if(k==1):
			print("match found for "+j)
		else:
			send.write(j)
			datalist.append(j)
	print("----New Items to be added----")
	p.close()
	c.close()
	send.close()
	for x in datalist:
		print(x)
