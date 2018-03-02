import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import main
import ensure

class GUI:
	def __init__(self):
		self.master = tk.Tk()
		self.img_lable = Label(self.master, text="Dataset dir:")
		self.img_lable.grid(row=0)

		# self.progress = ttk.Progressbar(self.master, orient="horizontal",
  #                                       length=200, mode="determinate")
		
		self.e1 = Entry(self.master)
		self.e1.grid(row=0, column=1)
		
		Button(self.master, text="Browse", command=self.browsedatadir).grid(row=0, column=2)
		Button(self.master, text="Convert", command=self.convert).grid(row=3, column=1)
		
		self.master.mainloop()

	def browsedatadir(self):
		self.directory = filedialog.askdirectory()
		self.e1.insert(0,self.directory)
	def convert(self):
		lfmt = "xml"
		ifmt = "jpg"
		# main.convert(self.directory)
		res = ensure.ensure(self.directory, ifmt, lfmt)
		
		if res == "OK":
			print("Everything loooks good!")
		else:
			print(res)	

gui = GUI()

