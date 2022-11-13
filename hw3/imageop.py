from PIL import Image
import math
import matplotlib.pyplot as plt

def chctrLINEAR(img, a = 1, b = 0):
	if img == None:
		print("error occur in imageop.py:chctrLINEAR(img, a, b):")
		print("img is None.")
		return img

	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			val = a * img.getpixel((x, y)) + b
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG

def chctrEXPON(img, a = 1, b = 0):
	if img == None:
		print("error occur in imageop.py:chctrEXPON(img, a, b):")
		print("img is None.")
		return img

	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
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
		print("error occur in imageop.py:chctrLOG(img, a, b):")
		print("img is None.")
		return img
	if b <= 1:
		print("error occur in imageop.py:chctrLOG(img, a, b):")
		print("b must be bigger 1.")
		return img
	
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			val = math.log(a * img.getpixel((x, y)) + b)
			if val >= 255:
				val = 255
			resIMG.putpixel((x, y), int(val))
	return resIMG

def grayhhlight(img, lb = 0, ub = 255, hhlightV = 255, preserve = True):
	if img == None:
		print("error occurs in imageop.py:grayhhlight(img, lb, ub, preserve):")
		print("img is None.")
		return img
	if lb > ub:
		print("error occurs in imageop.py:grayhhlight(img, lb, ub, preserve):")
		print("lower bound is bigger than upper bound.")
		return img
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			val = img.getpixel((x, y))
			if val >= lb and val <= ub:
				val = hhlightV
			elif not preserve:
				val = 0
			resIMG.putpixel((x, y), int(val))
	return resIMG

def negative(img):
	if img == None:
		print("error occurs in imageop.py:negative:")
		print("img is None")
		return img
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

def auto_level(img):
	n = [0 for i in range(256)]
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for val in ravel(img):
		n[val] += 1
	for i in range(1, 256):
		n[i] += n[i - 1]
	for x in range(row):
		for y in range(col):
			res = n[int(img.getpixel((x, y)))]
			resIMG.putpixel((x, y), int(res * 255 // (row * col)))
	return resIMG

def ravel(img):
	arr = []
	row = img.size[0]
	col = img.size[1]
	for x in range(row):
		for y in range(col):
			arr.append(int(img.getpixel((x, y))))
	return arr

def bit_slicing(img, i):
	if i >= 8 or i < 0:
		print("error occurs in imageop.py:extract_bit:")
		print("the selected bit is out of range. selected bit:", i, ", but the vaild range is [0, 7].")
		return img
	if img == None:
		print("error occurs in imageop.py:extract_bit:")
		print("img is None")
		return img
	bmask = [255 & (1 << j) for j in range(8)]
	row = img.size[0]
	col = img.size[1]
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			val = int(img.getpixel((x, y)))
			resIMG.putpixel((x, y), val & bmask[i])
	return resIMG

def average_filter(img, rang = 3):
	if not (rang & 1):
		return img
	if img == None:
		print("error occurs in imageop.py:mask:")
		print("img is None")
		return None
	m = [[1 for j in range(rang)] for i in range(rang)]
	return general_filter(img, m, rang)

def average_filter_arr(arr, row, col, rang = 3):
	if not (rang & 1):
		return arr
	if arr == None:
		print("error occurs in imageop.py:mask:")
		print("img is None")
		return None
	m = [[1 for j in range(rang)] for i in range(rang)]
	return general_filter_arr(arr, row, col, m, rang)

def sharpen_filter(img, k = 1):
	"""
	unsharp masking
	"""
	row, col = img.size[0], img.size[1]
	f_ = average_filter(img, 3)
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			resIMG.putpixel((x, y), int((k + 1) * int(img.getpixel((x, y))) - k * int(f_.getpixel((x, y)))))
	return resIMG

def general_filter(img, mask, rang, regu = True):
	if not (rang & 1):
		return img
	if img == None:
		print("error occurs in imageop.py:mask:")
		print("img is None")
		return img
	if len(mask) == 0 or len(mask) != rang or len(mask[0]) != rang:
		print("error occurs in imageop.py:mask:")
		print("the size of mask isn't right")
		return img

	offset = rang // 2
	row, col = img.size[0], img.size[1]
	resIMG = Image.new("L", (row, col))
	val = [[0 for c in range(col)] for r in range(row)]

	for x in range(row):
		for y in range(col):
			val[x][y] = int(img.getpixel((x, y)))

	for x in range(row):
		for y in range(col):
			newval = 0
			Sum = 0
			for s in range(-offset, offset + 1):
				for t in range(-offset, offset + 1):
					nx, ny = x + s, y + t
					if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
					newval += mask[s + offset][t + offset] * val[nx][ny]
					Sum += mask[s + offset][t + offset]
			if Sum != 0 and regu:
				newval //= Sum
			resIMG.putpixel((x, y), newval)
	return resIMG

def general_filter_arr(arr, row, col, mask, rang, regu = True):
	if not (rang & 1):
		return arr
	if arr == None:
		print("error occurs in imageop.py:general_filter_arr:")
		print("arr is None")
		return arr
	if len(mask) == 0 or len(mask) != rang or len(mask[0]) != rang:
		print("error occurs in imageop.py:general_filter_arr:")
		print("the size of mask isn't right")
		return arr

	offset = rang // 2
	val = arr.copy()

	for x in range(row):
		for y in range(col):
			newval = 0
			Sum = 0
			for s in range(-offset, offset + 1):
				for t in range(-offset, offset + 1):
					nx, ny = x + s, y + t
					if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
					newval += mask[s + offset][t + offset] * val[nx][ny]
					Sum += mask[s + offset][t + offset]
			if Sum != 0 and regu:
				newval //= Sum
			val[x][y] = newval
	return val

def median_filter(img, rang = 3):
	if img == None:
		print("error occurs in imageop.py:mask:")
		print("img is None")
		return img
	if not (rang & 1):
		return img
	row, col = img.size[0], img.size[1]
	offset = rang // 2
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			arr = []
			for s in range(-offset, offset + 1):
				for t in range(-offset, offset + 1):
					nx, ny = x + s, y + t
					if nx < 0 or ny < 0 or nx >= row or ny >= col: continue
					arr.append(int(img.getpixel((nx, ny))))
			l = len(arr)
			arr.sort()
			if l & 1:
				resIMG.putpixel((x, y), arr[l // 2])
			else:
				resIMG.putpixel((x, y), (arr[l // 2] + arr[l // 2 - 1]) // 2)
	return resIMG

def Laplacian_filter(img):
	if img == None:
		print("error occurs in imageop.py:Laplacian_mask:")
		print("img is None")
		return img
	row, col = img.size[0], img.size[1]
	m = [[1,1,1],
		 [1,-8,1],
		 [1,1,1]]
	LM = general_filter(img, m, 3, False)
	resIMG = Image.new("L", (row, col))
	for x in range(row):
		for y in range(col):
			resIMG.putpixel((x, y), img.getpixel((x, y)) - LM.getpixel((x, y)))
	return resIMG

def rgb_to_hsi(img):
	if img == None:
		print("error occurs in imageop.py:rgb_to_hsi:")
		print("img is None")
		return img
	row, col = img.size[0], img.size[1]
	hsi_arr = [[[0,0,0] for j in range(col)] for i in range(row)]
	for i in range(row):
		for j in range(col):
			r, g, b = img.getpixel((i, j))
			m = min(r, g, b)
			I = (r+g+b)/3
			S = (1-m/I if I>0 else 0)
			if g >= b:
				if math.fabs(r*r + g*g + b*b - r*g - r*b - g*b) <= 1e-5:
					H = 0 # white or black
				else:
					#print((r - 0.5*g - 0.5*b), (math.sqrt(r*r + g*g + b*b - r*g - r*b - g*b)))
					H = math.acos((r - 0.5*g - 0.5*b)/(math.sqrt(r*r + g*g + b*b - r*g - r*b - g*b))) / (2*math.pi) * 360
			elif b > g:
				if math.fabs(r*r + g*g + b*b - r*g - r*b - g*b) <= 1e-5:
					H = 0
				else:
					#print((r - 0.5*g - 0.5*b), (math.sqrt(r*r + g*g + b*b - r*g - r*b - g*b)))
					H = math.acos((r - 0.5*g - 0.5*b)/(math.sqrt(r*r + g*g + b*b - r*g - r*b - g*b))) / (2*math.pi) * 360
					H = 360 - H
			hsi_arr[i][j] = [H, S, I]
	#print(hsi_arr)
	return hsi_arr

def hsi_to_rgb(hsi_arr, row, col):
	resIMG = Image.new("RGB", (row, col))
	for i in range(row):
		for j in range(col):
			H, S, I = hsi_arr[i][j]
			if H == 0:
				r = I + 2*I*S
				g = I - I*S
				b = I - I*S
			elif 0 < H < 120:
				r = I + I*S* math.cos(H /360*2*math.pi)/math.cos((60-H) /360*2*math.pi)
				g = I + I*S* (1 - math.cos(H /360*2*math.pi)/math.cos((60-H) /360*2*math.pi))
				b = I - I*S
			elif H == 120:
				r = I - I*S
				g = I + 2*I*S
				b = I - I*S
			elif 120 < H < 240:
				r = I - I*S
				g = I + I*S* math.cos((H-120) /360*2*math.pi)/math.cos((180-H) /360*2*math.pi)
				b = I + I*S* (1 - math.cos((H-120) /360*2*math.pi)/math.cos((180 - H) /360*2*math.pi))
			elif H == 240:
				r = I - I*S
				g = I - I*S
				b = I + 2*I*S
			elif 240 < H < 360:
				r = I + I*S* (1-math.cos((H-240) /360*2*math.pi)/math.cos((300-H) /360*2*math.pi))
				g = I - I*S
				b = I + I*S* math.cos((H-240) /360*2*math.pi)/math.cos((300-H) /360*2*math.pi)
			else:
				print("error")
				return resIMG
			r, g, b = int(r),  int(g), int(b)
			resIMG.putpixel((i, j), (r, g, b))
	return resIMG
