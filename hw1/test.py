from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
from tkinter import ttk
from chctr import *
from rotate import *
from resize import *
from grayslice import *
from negative import *

class dialog():
	def __init__(self, window, n):
		self.n = n
		self.top = tkinter.Toplevel(window)
		self.top.geometry("750x250")

		self.entries = []
		self.inputs = [None] * n
		for i in range(n):
			self.entries.append(tkinter.Entry(self.top, width = 25))
			self.entries[i].pack()
		btn = tkinter.Button(self.top, text = "Submit", command = lambda: self.submit())
		btn.pack()

	def submit(self):
		for i in range(self.n):
			self.inputs[i] = self.entries[i].get()
		print(self.inputs)
		self.top.destroy()

def main():
	window = tkinter.Tk()
	window.geometry("1920x1080")
	window.title("DIP HW1")

	app = dialog(window, 3)
	window.mainloop()
	
	#new = chctrLINEAR(img, 1, -50)
	#new = chctrEXPON(img, 0.1, 1)
	#new = chctrLOG(img, 1e9, 2)
	#new = rotate(img, 12, expand = True)
	#new = resize(img, 200)
	#new = grayhhlight(img, 50, 100, hhlightV = 200, preserve = True)
	#new = negative(img)

	#img.show()
	#new.show()

if __name__ == "__main__":
	main()
