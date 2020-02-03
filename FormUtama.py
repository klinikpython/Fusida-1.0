# file: formutama.py

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as mb
import tkinter.filedialog as fd
import os
from PIL import ImageTk, Image
import sqlite3 as lite


class FormUtama:
	def __init__(self, parent):
		self.parent = parent
		
		self.parent.geometry("640x480")
		self.parent.title(":: Fusida 1.0 ::")
		
		self.atur_database()
		self.atur_metode()
		self.atur_komponen()
		
	def atur_database(self):
		pass

	def atur_metode(self):
		pass
		
	def atur_komponen(self):
		pass
		
		
class AturDatabase:
	def __init__(self):
		pass
		
	
class AturMetode:
	def __init__(self):
		pass
		
		
class AturKomponen:
	def __init__(self):
		pass


if __name__ == '__main__':
	root = tk.Tk()
	
	app = FormUtama(root)
	
	root.mainloop()
