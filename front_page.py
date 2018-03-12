import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import main
import ensure
import preprocess as p

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
		Button(self.master, text="Preprocess", command=self.preprocess).grid(row=3, column=2)
		self.master.mainloop()

	def browsedatadir(self):
		self.directory = filedialog.askdirectory()
		self.e1.insert(0,self.directory)

	def preprocess(self):
		print ("started preprocessing!")
		p.junk_remover(self.directory)
		p.junk_remover(self.directory, target="images", source="labelsxml", ext='jpg', fol="lost")
		p.renamifier(self.directory,"images")
		p.renamifier(self.directory,"labelsxml")
		
		print ("preprocessing completed!")

	def convert(self):
		lfmt = "xml"
		ifmt = "jpg"
		res = ensure.ensure(self.directory, ifmt, lfmt)
		
		if res == "OK":
			print("Everything loooks good!")
			#main.convert(self.directory)

		else:
			print(res)	

gui = GUI()

