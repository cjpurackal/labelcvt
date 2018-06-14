import tkinter as tk
from tkinter import *
import os


class Main_Gui:
	def __init__(self):
		self.master=tk.Tk()
		self.master.title("Main Page")
		self.classification_button=Button(self.master,text="Classification",command=self.classification)
		self.classification_button.grid(row=0,column=1,padx=(100,0),pady=(20,0))
		self.detection_button=Button(self.master,text="Dectection",command=self.detection)
		self.detection_button.grid(row=1,column=1,padx=(100,0),pady=(10,0),sticky="ew")
		self.segmentation_button=Button(self.master,text="Segmentation",command=self.classification)
		self.segmentation_button.grid(row=2,column=1,padx=(100,0),pady=(10,0))

		self.master.geometry("300x200")
		self.master.mainloop()
	def classification():
		pass
	def detection(self):
		os.system('python3 front_page.py')


gui=Main_Gui()