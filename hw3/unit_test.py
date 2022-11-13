import PIL
import imageop
import matplotlib.pyplot as plt
#img = PIL.Image.open("./testdata/elaine.512.tiff").convert("L")
#img = PIL.Image.open("./testdata/lenna.tif").convert("RGB")
#img = PIL.Image.open("./testdata/Lenna_512_color.tif").convert("RGB")
img = PIL.Image.open("./testdata/RGB.png").convert("RGB")

#with open("./testdata/pirate_a.raw", 'rb') as f:
#	img = PIL.Image.frombytes("L", (512, 512), f.read(), 'raw')

img.show()
hsi_arr = imageop.rgb_to_hsi(img)
i_arr = [[0 for j in range(img.size[1])] for i in range(img.size[0])]

for i in range(img.size[0]):
	for j in range(img.size[1]):
		i_arr[i][j] = hsi_arr[i][j][2]

newi_arr = imageop.average_filter_arr(i_arr, img.size[0], img.size[1], rang = 5)

for i in range(img.size[0]):
	for j in range(img.size[1]):
		hsi_arr[i][j][2] = newi_arr[i][j]

newimg = imageop.hsi_to_rgb(hsi_arr, img.size[0], img.size[1])
#newimg = imageop.average_filter(img, 3)
#newimg = imageop.general_filter(img, [[1,1,1],[1,1,1],[1,1,1]], 3)
#newimg = imageop.extract_bit(img, i)
#newimg = imageop.sharpen_filter(img, 1)
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
