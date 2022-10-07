import imageop
from dialog import *
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk

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
		self.path = None

	def Open(self):
		self.path = ursel_open_file()
		if not self.path:
			return
		self.filetype = self.path[self.path.rfind('.'):]
		if self.img == None:
			self.img = Image.open(self.path).convert("L")
			self.oimg = self.img
			self.photo = ImageTk.PhotoImage(self.img)
			self.row, self.col = self.img.size[0], self.img.size[1]
			self.canv_size = 1820, 980#int(math.sqrt(self.row * self.row + self.col * self.col) + 1)
			self.canvas = tkinter.Canvas(self.win, width = self.canv_size[0] , height = self.canv_size[1])
			self.canvasSP = self.canvas.create_image(self.canv_size[0]//2, self.canv_size[1]//2, anchor = tkinter.CENTER, image = self.photo)
			#self.canvasSP = self.canvas.create_image(100, 10, anchor = tkinter.NW, image = self.photo)
			self.canvas.grid(row = 0, column = 0)
		else:
			self.img = Image.open(self.path).convert("L")
			self.oimg = self.img
			self.updateCanvas()

	def Save(self):
		if not self.path:
			print("Error occurs in Canv.py:Save(self):")
			print("Trying to save nothing.")
			return
		self.img.save(self.path)
	def SaveAs(self):
		fpath = ursel_save_file(self.filetype)
		if not fpath:
			return
		self.img.save(fpath)

	def updateCanvas(self):
		self.photo = ImageTk.PhotoImage(self.img)
		#self.img.show()
		self.row, self.col = self.img.size[0], self.img.size[1]
		self.canvas.delete(self.canvasSP)
		#self.canvas.config(width = self.row, height = self.col)
		self.canvasSP = self.canvas.create_image(self.canv_size[0]//2, self.canv_size[1]//2, anchor = tkinter.CENTER, image = self.photo)
		#self.canvasSP = self.canvas.create_image(100, 10, anchor = tkinter.NW, image = self.photo)

	def chctrLINEAR(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		if a == '':	a = 1
		if b == '': b = 0
		a = float(a)
		b = float(b)
		self.oimg = self.img
		self.img = imageop.chctrLINEAR(self.img, a, b)
		self.updateCanvas()

	def chctrEXPON(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		if a == '':	a = 1
		if b == '': b = 0
		a = float(a)
		b = float(b)
		self.oimg = self.img
		self.img = imageop.chctrEXPON(self.img, a, b)
		self.updateCanvas()

	def chctrLOG(self):
		ask = dialog(self.win, 2, ["a", "b"])
		self.win.wait_window(ask.top)
		a, b = ask.inputs[0], ask.inputs[1]
		if a == None or b == None:
			return
		if a == '':	a = 1
		if b == '': b = 0
		a = float(a)
		b = float(b)
		self.oimg = self.img
		self.img = imageop.chctrLOG(self.img, a, b)
		self.updateCanvas()

	def rotate(self):
		ask = dialog(self.win, 1, ["ang"])
		self.win.wait_window(ask.top)
		ang = ask.inputs[0]
		if ang == None:	return
		if ang == '': ang = 0
		ang = float(ang)
		self.oimg = self.img
		self.img = imageop.rotate(self.oimg, ang, expand = True)
		self.updateCanvas()

	def resize(self):
		ask = dialog(self.win, 1, ["percentage(%)"])
		self.win.wait_window(ask.top)
		per = ask.inputs[0]
		if per == None:	return
		if per == '': per = 100
		per = int(per)
		self.oimg = self.img
		self.img = imageop.resize(self.img, per)
		self.updateCanvas()

	def grayhhlight(self):
		ask = dialog(self.win, 4, ["lower bound", "upper bound", "highlight value", "shall preserve?(True, False)"])
		self.win.wait_window(ask.top)
		lb, ub, hhlightV, preserve = ask.inputs[0], ask.inputs[1], ask.inputs[2], ask.inputs[3]
		if lb == None or ub == None or hhlightV == None or preserve == None:
			return
		if lb == '': lb = 0
		if ub == '': ub = 255
		if hhlightV == '': hhlightV = 255
		if preserve == '': preserve = "false"
		lb = int(lb)
		ub = int(ub)
		hhlightV = int(hhlightV)
		preserve = preserve.lower() in ['true', '1', 'y']
		self.oimg = self.img
		self.img = imageop.grayhhlight(self.img, lb, ub, hhlightV, preserve)
		self.updateCanvas()

	def negative(self):
		self.oimg = self.img
		self.img = imageop.negative(self.img)
		self.updateCanvas()

	def auto_level(self):
		self.oimg = self.img
		self.img = imageop.auto_level(self.img)
		self.updateCanvas()
	
	def bit_slicing(self):
		ask = dialog(self.win, 1, ["which bit"])
		self.win.wait_window(ask.top)
		i = ask.inputs[0]
		if i == None: return
		if i == "": i = 7
		i = int(i)
		if i > 7 or i < 0: return
		self.oimg = self.img
		self.img = imageop.bit_slicing(self.img, i)
		self.updateCanvas()

	def average_filter(self):
		ask = dialog(self.win, 1, ["degree"])
		self.win.wait_window(ask.top)
		r = ask.inputs[0]
		if r == None: return
		if r == "": r = 3
		r = int(r)
		if r < 0: return
		self.oimg = self.img
		self.img = imageop.average_filter(self.img, r)
		self.updateCanvas()
	
	def sharpen_filter(self):
		ask = dialog(self.win, 1, ["degree"])
		self.win.wait_window(ask.top)
		k = ask.inputs[0]
		if k == None: return
		if k == "": k = 1
		k = int(k)
		if k < 0: return
		self.oimg = self.img
		self.img = imageop.sharpen_filter(self.img, k)
		self.updateCanvas()
	
	def median_filter(self):
		ask = dialog(self.win, 1, ["size of region"])
		self.win.wait_window(ask.top)
		r = ask.inputs[0]
		if r == None: return
		if r == "": r = 3
		r = int(r)
		if r < 0: return
		self.oimg = self.img
		self.img = imageop.median_filter(self.img, r)
		self.updateCanvas()
	
	def Laplacian_filter(self):
		self.oimg = self.img
		self.img = imageop.Laplacian_filter(self.img)
		self.updateCanvas()
