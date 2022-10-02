from PIL import Image
import math

def chctrLINEAR(img, a = 1, b = 0):
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

def chctrEXPON(img, a = 1, b = 0):
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
				#print(img.getpixel((x, y)), end = ' ')
				val = math.exp(a * img.getpixel((x, y)) + b)
				#print(val)
			except OverflowError:
				val = 255
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG

def chctrLOG(img, a = 1, b = 0):
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

def grayhhlight(img, lb = 0, ub = 255, hhlightV = 255, preserve = True):
	if img == None:
		print("error occurs in grayslice.py:grayhhlight(img, lb, ub, preserve):")
		print("img is None.")
		return None
	if lb > ub:
		print("error occurs in grayslice.py:grayhhlight(img, lb, ub, preserve):")
		print("lower bound is bigger than upper bound.")
		return img
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(1, row):
		for y in range(1, col):
			val = img.getpixel((x, y))
			if val >= lb and val <= ub:
				val = hhlightV
			elif not preserve:
				val = 0
			resIMG.putpixel((x, y), int(val))
	return resIMG

def negative(img):
	if img == None:
		print("error occurs in negative.py:negative:")
		print("img is None")
		return None
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			resIMG.putpixel((x, y), int(255 - img.getpixel((x, y)) + 1))
	return resIMG

def resize(img, perc = 50,  resample = Image.Resampling.BILINEAR):
	return img.resize((img.size[0] * perc // 100, img.size[1] * perc // 100), resample)

def rotate(img, ang = 90, expand = True):
	return img.rotate(ang, expand = expand)
