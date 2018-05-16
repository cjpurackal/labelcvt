#!/usr/bin/env python3
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import main
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
from plot import draw
from server import serverutil
import frameworks.yolo as ycg
import matplotlib.pyplot as plt 
import matplotlib.patches as patches
from PIL import Image
import numpy as np
class GUI:
	def __init__(self):
		self.master = tk.Tk()
		self.img_lable = Label(self.master, text="Dataset dir:")
		self.img_lable.grid(row=0)

		self.progress = ttk.Progressbar(self.master, orient="horizontal",
  		                                 length=200, mode="indeterminate")
		#self.progress.grid(row=6,column=1)
		
		self.e1 = Entry(self.master)
		self.e1.grid(row=0, column=1)
		
		Button(self.master, text="Browse", command=self.browsedatadir).grid(row=0, column=2)
		Button(self.master, text="Convert", command=self.convert).grid(row=3, column=1)		
		Button(self.master, text="Preprocess", command=self.preprocess).grid(row=3, column=2)
		
		Button(self.master, text="Yolo Zip", command=self.yolo_zip).grid(row=4, column=2)
		Button(self.master,text="Clean",command=self.clean_dir).grid(row=5,column=2)
		Button(self.master,text="Upload",command=self.upload).grid(row=6,column=2)
		Button(self.master,text="Visualize",command=self.visual).grid(row=7,column=2)
		self.master.mainloop()

	def browsedatadir(self):
		self.directory = filedialog.askdirectory()
		self.e1.insert(0,self.directory)


	def visual(self):
		newWindow=tk.Toplevel(self.master)

		self.xmin_label=Label(newWindow,text="Xmin : ")
		self.xmin_label.grid(row=0,column=1)
		self.xmin_input=Entry(newWindow,bd=1)
		
		self.xmin_input.grid(row=0,column=2)
		self.ymin_label=Label(newWindow,text="Ymin : ")
		self.ymin_label.grid(row=1,column=1)
		self.ymin_input=Entry(newWindow,bd=1)
		self.ymin_input.grid(row=1,column=2)

		self.xmax_label=Label(newWindow,text="Xmax : ")
		self.xmax_label.grid(row=2,column=1)
		self.xmax_input=Entry(newWindow,bd=1)
		self.xmax_input.grid(row=2,column=2)
		self.ymax_label=Label(newWindow,text="Ymax : ")
		self.ymax_label.grid(row=3,column=1)
		self.ymax_input=Entry(newWindow,bd=1)
		self.ymax_input.grid(row=3,column=2)

		self.browse_label=Label(newWindow,text="Browse : ")
		self.browse_label.grid(row=4,column=1)
		self.browse_path=Entry(newWindow)
		self.browse_path.grid(row=4,column=2)
		self.browse_button=Button(newWindow,text="Browse",command=self.askfile).grid(row=4,column=3)

		Button(newWindow,text="Plot",command=self.plot).grid(row=5,column=2)
		newWindow.geometry("300x200")

	def askfile(self):
		self.file=filedialog.askopenfilename()
		self.browse_path.insert(0,self.file)
		self.original_path=self.browse_path.get()
		print(self.original_path)
	def plot(self):
		self.xmin=self.xmin_input.get()
		self.ymin=self.ymin_input.get()
		self.xmax=self.xmax_input.get()
		self.ymax=self.ymax_input.get()
		print(int(self.xmin))
		x=int(self.xmin)
		y=int(self.ymin)
		xm=int(self.xmax)
		ym=int(self.ymax)
		
		#print(path_file)
		draw.imageplot(x,y,xm,ym,self.original_path)
		#draw.imageplot(self.xmin,self.ymin,self.xmax,self.ymax)

		

	#compare function
	def upload(self):
		serverutil.filestosend(self)
		

	#clean function
			
	def clean_dir(self):
		print("Cleaning in progress")
		print("-----Listing folders-----")
		for subdirs in os.listdir(self.directory):
			print(subdirs)
			if(subdirs=="images" or subdirs=="labelsxml"):
				print ("found images/labelsxml")
			else:
				print("deleting dir : " + subdirs)
				if(os.path.isfile(subdirs)):
					os.remove(subdirs)
				shutil.rmtree(os.path.join(self.directory, subdirs),ignore_errors=False,onerror=None)				
				
				
	

	def preprocess(self):
		self.progress.grid(row=6,column=1)
		self.progress.start([5])
		lfmt = "xml"
		ifmt = "jpg"
		print ("started preprocessing!")
		p.renamifier(self.directory,"images")
		p.renamifier(self.directory,"labelsxml")
		p.junk_remover(self.directory)
		p.junk_remover(self.directory, target="images", source="labelsxml", ext='jpg', fol="lost")
				
		print ("preprocessing completed!")
		self.progressingBar()
		
	def progressingBar(self):
		print("Stop Progress")
		self.progress.stop()
		self.progress.grid_forget()
		#self.newWindow()
		
	def convert(self):
		self.progress.grid(row=6,column=1)
		self.progress.start(5)
		lfmt = "xml"
		ifmt = "jpg"
		res = ensure.ensure(self.directory, ifmt, lfmt)
		
		if res == "OK":
			print("Everything loooks good!")
			main.update_cat_names(self.directory)
			main.convert(self.directory)
			print("Here")
			self.progressingBar()
		else:
			print(res)	
		

	def yolo_zip(self):
		ypath = os.path.join(self.directory,"yolo_zip")
		if not os.path.exists(ypath):
			os.mkdir(ypath)
		if not os.path.exists(ypath+"/dataset"):
			os.mkdir(ypath+"/dataset")
			
			
		os.system("cp {}/images/*/* {}/dataset".format(self.directory, ypath))
		os.system("cp {}/labelsyolo/*/* {}/dataset".format(self.directory, ypath))
		os.system("cp cat.names {}".format(ypath))

		#get the count of cats
		cats = open("cat.names",'r')
		nc = sum(1 for cat in cats)

		y = ycg.Yolo(nc)
		y.set_root(self.directory)
		y.set_server_path("/home/ubuntu/packages/yolov3/darknet/dataset")
		y.preprocess(ypath)
		y.generate_conf(ypath)
		y.generate_test_train_files(ypath)
		y.generate_data_file(ypath)

		os.system("zip -r {}/yolo.zip {}".format(ypath,ypath))


		


gui = GUI()

