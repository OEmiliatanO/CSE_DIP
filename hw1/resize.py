from PIL import Image

def resize(img, perc,  resample = Image.Resampling.BILINEAR):
	return img.resize((img.size[0] * perc // 100, img.size[1] * perc // 100), resample)
