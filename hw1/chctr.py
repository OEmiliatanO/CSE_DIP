from PIL import Image
import math

def chctrLINEAR(img, a, b):
	if img == None:
		print("error occur in chctr.py:chctrLINEAR(img, a, b):")
		print("img is None.")
		return None

	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(1, row):
		for y in range(1, col):
			val = a * img.getpixel((x, y)) + b
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG

def chctrEXPON(img, a, b):	
	if img == None:
		print("error occur in chctr.py:chctrEXPON(img, a, b):")
		print("img is None.")
		return None

	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(1, row):
		for y in range(1, col):
			try:
				val = math.exp(a * img.getpixel((x, y)) + b)
			except OverflowError:
				val = 255
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG

def chctrLOG(img, a, b):
	if img == None:
		print("error occur in chctr.py:chctrLOG(img, a, b):")
		print("img is None.")
		return None
	if b <= 1:
		print("error occur in chctr.py:chctrLOG(img, a, b):")
		print("b must be bigger 1.")
		return img
	
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(1, row):
		for y in range(1, col):
			val = math.log(a * img.getpixel((x, y)) + b)
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG


