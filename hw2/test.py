import PIL
import imageop
import matplotlib.pyplot as plt
#img = PIL.Image.open("./testdata/elaine.512.tiff").convert("L")
#img = PIL.Image.open("./testdata/lenna_gray.tif").convert("L")

with open("./testdata/pirate_a.raw", 'rb') as f:
	img = PIL.Image.frombytes("L", (512, 512), f.read(), 'raw')

img.show()
#newimg = imageop.average_filter(img, 3)
#newimg = imageop.general_filter(img, [[1,1,1],[1,1,1],[1,1,1]], 3)
#newimg = imageop.extract_bit(img, i)
#newimg = imageop.sharpen_filter(img, 1)
newimg = imageop.median_filter(img, 3)
#newimg = imageop.auto_level(img)
#newimg.show()
#newimg = imageop.Laplacian_filter(newimg)
newimg.show()

"""
ohis = imageop.ravel(img)
nhis = imageop.ravel(newimg)
fig, axs = plt.subplots(1, 2)
axs[0].hist(ohis, bins = 256, range = (0, 255))
axs[1].hist(nhis, bins = 256, range = (0, 255))
plt.show()
"""
