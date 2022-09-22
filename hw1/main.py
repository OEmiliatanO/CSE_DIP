from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
from chctr import *
from rotate import *
from resize import *
from grayslice import *
from negative import *
import math

def ursel_open_file():
	fname = filedialog.askopenfilename(initialdir = "./", title = "Select a File")
	return fname

def ursel_save_file():
	fname = filedialog.asksaveasfile(mode = 'w', initialdir = "./")
	return fname

class Canv:
	"""
	chctrLINEAR(img, 1, -50)
	chctrEXPON(img, 0.1, 1)
	chctrLOG(img, 1e9, 2)
	rotate(img, 12, expand = True)
	resize(img, 200)
	grayhhlight(img, 50, 100, hhlightV = 200, preserve = True)
	negative(img)
	"""
	def __init__(self, win):
		self.canvas = None
		self.img = None
		self.photo = None
		self.win = win
		self.row = None
		self.col = None
		self.canvasSP = None
		self.canv_size = None

	def Open(self):
		fpath = ursel_open_file()
		print("the open path: ", fpath)
		if fpath == None:
			return
		self.img = Image.open(fpath).convert("L")
		self.photo = ImageTk.PhotoImage(self.img)
		#self.img.show()
		self.row, self.col = self.img.size[0], self.img.size[1]
		self.canv_size = int(math.sqrt(self.row * self.row + self.col * self.col) + 1)
		print("canv_size:", self.canv_size)
		self.canvas = tkinter.Canvas(self.win, width = self.canv_size , height = self.canv_size)
		self.canvasSP = self.canvas.create_image(self.canv_size//2, self.canv_size//2, anchor = tkinter.CENTER, image = self.photo)
		self.canvas.pack()

	def Save(self):
		fpath = ursel_save_file()
		print("the save path: ", fpath)
		if fpath == None:
			return
		self.img.save(fpath)

	def updateCanvas(self):
		self.photo = ImageTk.PhotoImage(self.img)
		#self.img.show()
		self.row, self.col = self.img.size[0], self.img.size[1]
		self.canvas.delete(self.canvasSP)
		#self.canvas.config(width = self.row, height = self.col)
		self.canvasSP = self.canvas.create_image(self.canv_size//2, self.canv_size//2, anchor = tkinter.CENTER, image = self.photo)

	def chctrLINEAR(self):
		a, b = 1, 0 #TODO
		self.img = chctrLINEAR(self.img, a, b)
		self.updateCanvas()
	def chctrEXPON(self):
		a, b = 1, 0 #TODO
		self.img = chctrEXPON(self.img, a, b)
		self.updateCanvas()
	def chctrLOG(self):
		a, b = 1, 2 #TODO
		self.img = chctrLOG(self.img, a, b)
		self.updateCanvas()
	def rotate(self):
		ang = 45 #TODO
		self.img = rotate(self.img, ang, expand = True)
		self.updateCanvas()
	def resize(self):
		per = 100 #TODO
		self.img = resize(self.img, per)
		self.updateCanvas()
	def grayhhlight(self):
		lb, ub, hhlightV, preserve = 50, 100, 200, True #TODO
		self.img = grayhhlight(self.img, lb, ub, hhlightV, preserve)
		self.updateCanvas()
	def negative(self):
		self.img = negative(self.img)
		self.updateCanvas()

def main():
	window = tkinter.Tk()
	window.geometry("1920x1080")
	window.title("DIP HW1")
	canv = Canv(window)
	menubar = tkinter.Menu(window)
	
	filemenu = tkinter.Menu(menubar)
	filemenu.add_command(label = "Open", command = lambda: canv.Open())
	filemenu.add_command(label = "Save", command = lambda: canv.Save())
	
	editmenu = tkinter.Menu(menubar)
	
	chctrmenu = tkinter.Menu(editmenu)
	chctrmenu.add_command(label = "linear", command = lambda: canv.chctrLINEAR())
	chctrmenu.add_command(label = "exponentially", command = lambda: canv.chctrEXPON())
	chctrmenu.add_command(label = "logarithmically", command = lambda: canv.chctrLOG())
	
	editmenu.add_cascade(label = "change constrast", menu = chctrmenu)

	editmenu.add_command(label = "rotate", command = lambda: canv.rotate())
	editmenu.add_command(label = "resize", command = lambda: canv.resize())
	editmenu.add_command(label = "gray-level slicing", command = lambda: canv.grayhhlight())
	editmenu.add_command(label = "negative", command = lambda: canv.negative())
	
	menubar.add_cascade(label = "File", menu = filemenu)
	menubar.add_cascade(label = "Edit", menu = editmenu)

	window['menu'] = menubar
	
	window.mainloop()

if __name__ == "__main__":
	main()
