import imageop
from dialog import *
import tkinter
from tkinter import filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

def ursel_open_file():
	fname = filedialog.askopenfilename(initialdir = "./", title = "Select a Image", filetypes = [
		("image", "*.jpg *.png *.tif *.tiff *.raw"),
		("jpg", "*.jpg"),
		("png", "*.png"),
		("tif", "*.tif"),
		("tiff", "*.tiff"),
		("raw", "*.raw"),
	])
	return fname

def ursel_save_file(defaultFile):
	fname = filedialog.asksaveasfilename(initialdir = "./", filetypes = [
		("original type", defaultFile),
		("jpg", ".jpg"),
		("png", ".png"),
		("tif", ".tif"),
		("tiff", ".tiff")
	])
	return fname

class Canv:
	def __init__(self, win):
		self.win = win
		
		self.canvasShow = None
		self.canvasOper = None
		
		self.imgShow = None
		self.imgOper = None
		
		self.photoShow = None
		self.photoOper = None
		
		self.rowShow, self.colShow = None, None
		self.rowOper, self.colOper = None, None
		
		self.canvasShowSP = None
		self.canvasOperSP = None

		self.canv_size = None
		self.filetype = None
		self.path = None

	def Open(self):
		self.path = ursel_open_file()
		if not self.path:
			return
		self.filetype = self.path[self.path.rfind('.'):]
		if self.imgShow == None:
			if self.filetype == ".raw":
				with open(self.path, 'rb') as f:
					self.imgShow = Image.frombytes("L", (512, 512), f.read(), 'raw')
				self.filetype = ".png"
				self.path = self.path[:self.path.rfind('.')] + self.filetype
			else: self.imgShow = Image.open(self.path).convert("L")
			self.imgOper = self.imgShow.copy()
			
			self.photoShow = ImageTk.PhotoImage(self.imgShow)
			self.photoOper = ImageTk.PhotoImage(self.imgOper)
			
			self.rowShow, self.colShow = self.imgShow.size[0], self.imgShow.size[1]
			self.rowOper, self.colOper = self.imgOper.size[0], self.imgOper.size[1]
			
			self.canvShow_size = self.imgShow.size
			self.canvOper_size = self.imgOper.size

			self.canvasShow = tkinter.Canvas(self.win, width = self.canvShow_size[0] , height = self.canvShow_size[1])
			self.canvasOper = tkinter.Canvas(self.win, width = self.canvOper_size[0] , height = self.canvOper_size[1])

			self.canvasShowSP = self.canvasShow.create_image(0, 0, anchor = tkinter.NW, image = self.photoShow)
			self.canvasOperSP = self.canvasOper.create_image(0, 0, anchor = tkinter.NW, image = self.photoOper)

			self.canvasShow.grid(row=0,column=0)
			self.canvasOper.grid(row=0,column=1)
		else:
			if self.filetype == ".raw":
				with open(self.path, 'rb') as f:
					self.imgShow = Image.frombytes("L", (512, 512), f.read(), 'raw')
				self.filetype = ".jpg"
				self.path = self.path[:self.path.rfind('.')] + self.filetype
			else: self.imgShow = Image.open(self.path).convert("L")
			self.imgOper = self.imgShow.copy()
			self.updateCanvas()

	def Save(self, which = "oper"):
		if not self.path:
			print("Error occurs in Canv.py:Save(self):")
			print("Trying to save nothing.")
			return
		if which == "oper":
			self.imgOper.save(self.path)
		elif which == "show":
			self.imgShow.save(self.path)

	def SaveAs(self, which = "oper"):
		self.path = ursel_save_file(self.filetype)
		if not self.path:
			return
		if which == "oper":
			self.imgOper.save(self.path)
		elif which == "show":
			self.imgShow.save(self.path)

	def updateCanvas(self):
		self.photoShow = ImageTk.PhotoImage(self.imgShow)
		self.photoOper = ImageTk.PhotoImage(self.imgOper)
		#self.img.show()
		self.rowShow, self.colShow = self.imgShow.size[0], self.imgShow.size[1]
		self.rowOper, self.colOper = self.imgOper.size[0], self.imgOper.size[1]
		self.canvasShow.delete(self.canvasShowSP)
		self.canvasOper.delete(self.canvasOperSP)
		#self.canvas.config(width = self.row, height = self.col)
		self.canvasShowSP = self.canvasShow.create_image(0, 0, anchor = tkinter.NW, image = self.photoShow)
		self.canvasOperSP = self.canvasOper.create_image(0, 0, anchor = tkinter.NW, image = self.photoOper)
		#self.canvasSP = self.canvas.create_image(100, 10, anchor = tkinter.NW, image = self.photo)
	
	def swap(self):
		self.imgShow, self.imgOper = self.imgOper, self.imgShow
		self.updateCanvas()
	def copyToOper(self):
		self.imgOper = self.imgShow.copy()
		self.updateCanvas()
	def copyToShow(self):
		self.imgShow = self.imgOper.copy()
		self.updateCanvas()

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
		self.imgOper = imageop.chctrLINEAR(self.imgShow, a, b)
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
		self.imgOper = imageop.chctrEXPON(self.imgShow, a, b)
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
		self.imgOper = imageop.chctrLOG(self.imgShow, a, b)
		self.updateCanvas()

	def rotate(self):
		ask = dialog(self.win, 1, ["ang"])
		self.win.wait_window(ask.top)
		ang = ask.inputs[0]
		if ang == None:	return
		if ang == '': ang = 0
		ang = float(ang)
		self.imgOper = imageop.rotate(self.imgShow, ang, expand = True)
		self.updateCanvas()

	def resize(self):
		ask = dialog(self.win, 1, ["percentage(%)"])
		self.win.wait_window(ask.top)
		per = ask.inputs[0]
		if per == None:	return
		if per == '': per = 100
		per = int(per)
		self.imgOper = imageop.resize(self.imgShow, per)
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
		self.imgOper = imageop.grayhhlight(self.imgShow, lb, ub, hhlightV, preserve)
		self.updateCanvas()

	def negative(self):
		self.imgOper = imageop.negative(self.imgShow)
		self.updateCanvas()

	def auto_level(self):
		self.imgOper = imageop.auto_level(self.imgShow)
		self.updateCanvas()
		hist1, hist2 = imageop.ravel(self.imgShow), imageop.ravel(self.imgOper)
		plt.hist(hist1, bins = 256, alpha = 0.5, label = 'original')
		plt.hist(hist2, bins = 256, alpha = 0.5, label = 'after')
		plt.legend(loc = 'best')
		plt.show()
	
	def bit_slicing(self):
		ask = dialog(self.win, 1, ["which bit"])
		self.win.wait_window(ask.top)
		i = ask.inputs[0]
		if i == None: return
		if i == "": i = 7
		i = int(i)
		if i > 7 or i < 0: return
		self.imgOper = imageop.bit_slicing(self.imgShow, i)
		self.updateCanvas()

	def average_filter(self):
		ask = dialog(self.win, 1, ["degree"])
		self.win.wait_window(ask.top)
		r = ask.inputs[0]
		if r == None: return
		if r == "": r = 3
		r = int(r)
		if r < 0: return
		self.imgOper = imageop.average_filter(self.imgShow, r)
		self.updateCanvas()
	
	def sharpen_filter(self):
		ask = dialog(self.win, 1, ["degree"])
		self.win.wait_window(ask.top)
		k = ask.inputs[0]
		if k == None: return
		if k == "": k = 1
		k = int(k)
		if k < 0: return
		self.imgOper = imageop.sharpen_filter(self.imgShow, k)
		self.updateCanvas()
	
	def median_filter(self):
		ask = dialog(self.win, 1, ["size of region"])
		self.win.wait_window(ask.top)
		r = ask.inputs[0]
		if r == None: return
		if r == "": r = 3
		r = int(r)
		if r < 0: return
		self.imgOper = imageop.median_filter(self.imgShow, r)
		self.updateCanvas()
	
	def Laplacian_filter(self):
		self.imgOper = imageop.Laplacian_filter(self.imgShow)
		self.updateCanvas()
