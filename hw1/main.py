from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
from chctr import *
from rotate import *
from resize import *
from grayslice import *
from negative import *
from dialog import *
import math

def ursel_open_file():
	fname = filedialog.askopenfilename(initialdir = "./", title = "Select a Image", filetypes = [
		("image", "*.jpg *.png *.tif"),
		("jpg", "*.jpg"),
		("png", "*.png"),
		("tif", "*.tif"),
	])
	return fname

def ursel_save_file(defaultFile):
	fname = filedialog.asksaveasfilename(initialdir = "./", filetypes = [
		("original type", defaultFile),
		("jpg", ".jpg"),
		("png", ".png"),
		("tif", ".tif"),
	])
	return fname

class Canv:
	"""
	chctrLINEAR(img, a, b)
	chctrEXPON(img, a, b)
	chctrLOG(img, a, b)
	rotate(img, ang, expand)
	resize(img, per)
	grayhhlight(img, lb, rb, hhlightV, preserve)
	negative(img)
	"""
	def __init__(self, win):
		self.canvas = None
		self.img = None
		self.oimg = None
		self.photo = None
		self.win = win
		self.row = None
		self.col = None
		self.canvasSP = None
		self.canv_size = None
		self.filetype = None

	def Open(self):
		fpath = ursel_open_file()
		if not fpath:
			return
		self.filetype = fpath[fpath.rfind('.'):]
		if self.img == None:
			self.img = Image.open(fpath).convert("L")
			self.oimg = self.img
			self.photo = ImageTk.PhotoImage(self.img)
			self.row, self.col = self.img.size[0], self.img.size[1]
			self.canv_size = 1000#int(math.sqrt(self.row * self.row + self.col * self.col) + 1)
			self.canvas = tkinter.Canvas(self.win, width = self.canv_size , height = self.canv_size)
			self.canvasSP = self.canvas.create_image(self.canv_size//2, self.canv_size//2, anchor = tkinter.CENTER, image = self.photo)
			self.canvas.pack()
		else:
			self.img = Image.open(fpath).convert("L")
			self.oimg = self.img
			self.updateCanvas()


	def Save(self):
		fpath = ursel_save_file(self.filetype)
		if not fpath:
			return
		print("save path:", fpath)
		self.img.save(fpath)

	def updateCanvas(self):
		self.photo = ImageTk.PhotoImage(self.img)
		#self.img.show()
		self.row, self.col = self.img.size[0], self.img.size[1]
		self.canvas.delete(self.canvasSP)
		#self.canvas.config(width = self.row, height = self.col)
		self.canvasSP = self.canvas.create_image(self.canv_size//2, self.canv_size//2, anchor = tkinter.CENTER, image = self.photo)

	def chctrLINEAR(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		a = float(a)
		b = float(b)
		self.img = chctrLINEAR(self.img, a, b)
		self.updateCanvas()

	def chctrEXPON(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		a = float(a)
		b = float(b)
		self.img = chctrEXPON(self.img, a, b)
		self.updateCanvas()

	def chctrLOG(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		a = float(a)
		b = float(b)
		self.img = chctrLOG(self.img, a, b)
		self.updateCanvas()

	def rotate(self):
		ask = dialog(self.win, 1, ["ang"])
		self.win.wait_window(ask.top)
		ang = ask.inputs[0]
		if ang == None:
			return
		ang = float(ang)
		self.img = rotate(self.oimg, ang, expand = True)
		self.updateCanvas()

	def resize(self):
		ask = dialog(self.win, 1, ["percentage"])
		self.win.wait_window(ask.top)
		per = ask.inputs[0]
		if per == None:
			return
		per = int(per)
		self.img = resize(self.img, per)
		self.updateCanvas()

	def grayhhlight(self):
		ask = dialog(self.win, 4, ["lower bound", "upper bound", "highlight value", "shall preserve?(True, False)"])
		self.win.wait_window(ask.top)
		lb, ub, hhlightV, preserve = ask.inputs[0], ask.inputs[1], ask.inputs[2], ask.inputs[3]
		if lb == None or ub == None or hhlightV == None or preserve == None:
			return
		lb = int(lb)
		ub = int(ub)
		hhlightV = int(hhlightV)
		preserve = preserve.lower() in ['true', '1', 'y']
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
