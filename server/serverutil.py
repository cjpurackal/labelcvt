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
	'''for x in os.listdir('/home/caroline/Desktop/data'):
		if (imghdr.what(os.path.join('/home/caroline/Desktop/data',x)) =="jpeg"):
			f.write(x+"\n")
	'''
		#server data
	#ssh
	#miniurl=self.directory+"/temp/"
	#Directory to upload
	miniurl="/home/caroline/agrima/datasets/capgemini/mini/more2/dataset/temp/"
	serverdata=os.popen("echo Jeffin0718 | sudo -S ssh -i /home/caroline/Downloads/agrima_p2xlarge_200.pem ubuntu@52.43.166.212 ls /home/ubuntu/packages/yolov3/darknet/dataset/*.jpg").read()
	individualnames=serverdata.split("\n")
	for o in individualnames:
		names=o.split("/")
		f.write(names[len(names)-1]+"\n")
	f.close()
	
	#ssh
	#file containg the names of images in the server
	r=open('/home/caroline/Desktop/data/data.txt','r+')

	fl=r.readlines()
	k=0
		#new upload
	#File containing the names of the images to be uploaded 
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
	
	p.close()
	c.close()
	send.close()
	if(len(datalist)==0):
		print("No new Data found!!!!")
	else:
		print("----New Items to be added----")
		
		for x in datalist:
			url1=miniurl+x
			print(url1)
			url="/home/caroline/agrima/datasets/capgemini/mini/more2/dataset/temp/apple_0.jpg"
			if(url==url1):
				print("equal")
			else:
				print("false")
			print (" sudo scp -i /home/caroline/Downloads/agrima_p2xlarge_200.pem "+ url+" ubuntu@52.43.166.212:~")
			os.system("echo Jeffin0718 | sudo scp -i  /home/caroline/Downloads/agrima_p2xlarge_200.pem "+url+" ubuntu@52.43.166.212:~")
			#os.system("echo Jeffin0718 | sudo scp -i  /home/caroline/Downloads/agrima_p2xlarge_200.pem "+url+" ubuntu@52.43.166.212:~")
			# print(x)
