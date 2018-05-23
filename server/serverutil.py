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
	h=(Path.home())
	print("Ready to compare files")
	i=0;
	datalist=[]
		
	#file containing the names of images syored in server
	#'/home/jeffin/Desktop/test/data.txt'
	serverfiles=str(h)+'/Desktop/test/data.txt'
	f=open(serverfiles,"w+")
	
		#server data
	#ssh
	#miniurl=self.directory+"/temp/"
	#Directory to upload
	miniurl="/home/jeffin/agrima/datasets/capgemini/mini/more2/temp/"
	miniurl1='/home/jeffin/agrima/datasets/capgemini/mini/more2/temp/'
	

	print(h)
	serverdata=os.popen("echo Jeffin | sudo -S ssh -i /home/jeffin/agrima/key/agrima_p2xlarge_200.pem ubuntu@52.43.166.212 ls /home/ubuntu/packages/yolov3/darknet/dataset/*.jpg").read()
	individualnames=serverdata.split("\n")
	for o in individualnames:
		names=o.split("/")
		f.write(names[len(names)-1]+"\n")
	f.close()
	
	#ssh
	#file containg the names of images in the new dataset
	newfiles=str(h)+'/Desktop/test/newdata.txt'
	#r=open(newfiles,'r+')
	#r=open('/home/jeffin/Desktop/test/data.txt','r+')

	
	k=0
		#new upload
	#File containing the names of the images to be uploaded 
	#'/home/jeffin/Desktop/test/newdata.txt'
	c=open(newfiles,"w+")
	print(self.directory)
	#os.path.join(self.directory,'temp')
	for img in os.listdir(miniurl):
		c.write(img+"\n")
	c.close()
	#'/home/jeffin/Desktop/test/newdata.txt'
	p=open(newfiles,"r+")
	newfilestoserver=str(h)+'/Desktop/test/senddata.txt'
	send=open(newfilestoserver,"w+")
	r=open(serverfiles,'r+')

	fl=r.readlines()
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
	server1="ubuntu@52.43.166.212:~/packages/yolov3/darknet/dataset/"
	p="/home/jeffin/agrima/datasets/capgemini/mini/more2/temp/apple_1v.jpg"
	if(len(datalist)==0):
		print("No new Data found!!!!")
	else:
		print("----New Items to be added----")
		tobesend=open(newfilestoserver,"r+")
		l=tobesend.readlines()

		items=0
		for k in l:
			items+=1
			print("uploading "+k+" to server")
			url2="/home/jeffin/agrima/datasets/capgemini/mini/more2/temp/"+k.strip()
			n="echo Jeffin | sudo scp -i /home/jeffin/agrima/key/agrima_p2xlarge_200.pem -r /home/jeffin/agrima/datasets/capgemini/mini/more2/temp/apple_1v.jpg ubuntu@52.43.166.212:~/packages/yolov3/darknet/dataset/"
			m="echo Jeffin | sudo scp -i /home/jeffin/agrima/key/agrima_p2xlarge_200.pem -r "+url2.strip()+" "+server1
			os.system(m)
		print(str(items)+ " items uploaded")
		
