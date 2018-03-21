import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import main
import ensure
import preprocess as p
from shutil import copy2
import os
import frameworks.yolo as ycg
class GUI:
	def __init__(self):
		self.master = tk.Tk()
		self.img_lable = Label(self.master, text="Dataset dir:")
		self.img_lable.grid(row=0)

		# self.progress = ttk.Progressbar(self.master, orient="horizontal",
  		#                                 length=200, mode="determinate")
		
		self.e1 = Entry(self.master)
		self.e1.grid(row=0, column=1)
		
		Button(self.master, text="Browse", command=self.browsedatadir).grid(row=0, column=2)
		Button(self.master, text="Convert", command=self.convert).grid(row=3, column=1)		
		Button(self.master, text="Preprocess", command=self.preprocess).grid(row=3, column=2)
		Button(self.master, text="Yolo Zip", command=self.yolo_zip).grid(row=4, column=2)
		self.master.mainloop()

	def browsedatadir(self):
		self.directory = filedialog.askdirectory()
		self.e1.insert(0,self.directory)

	def preprocess(self):
		lfmt = "xml"
		ifmt = "jpg"
		print ("started preprocessing!")
		p.renamifier(self.directory,"images")
		p.renamifier(self.directory,"labelsxml")
		p.junk_remover(self.directory)
		p.junk_remover(self.directory, target="images", source="labelsxml", ext='jpg', fol="lost")		
		print ("preprocessing completed!")
		
	def convert(self):
		lfmt = "xml"
		ifmt = "jpg"
		res = ensure.ensure(self.directory, ifmt, lfmt)
		
		if res == "OK":
			print("Everything loooks good!")
			main.update_cat_names(self.directory)
			main.convert(self.directory)

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
		y.set_server_path("/home/ubuntu/packages/darknet/dataset")
		y.preprocess(ypath)
		y.generate_conf(ypath)
		y.generate_test_train_files(ypath)
		y.generate_data_file(ypath)

		os.system("zip -r {}/yolo.zip {}".format(ypath,ypath))


		


gui = GUI()

