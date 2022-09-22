from PIL import Image

def grayhhlight(img, lb, ub, hhlightV = 255, preserve = True):
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
