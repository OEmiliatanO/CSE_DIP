from PIL import Image

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
