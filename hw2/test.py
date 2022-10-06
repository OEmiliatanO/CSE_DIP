import PIL
import imageop
import matplotlib.pyplot as plt
img = PIL.Image.open("./testdata/elaine.512.tiff").convert("L")
#img = PIL.Image.open("./testdata/lenna_gray.tif").convert("L")
img.show()
ohis = imageop.ravel(img)
newimg = imageop.auto_level(img)
newimg.show()
nhis = imageop.ravel(newimg)
fig, axs = plt.subplots(1, 2)
axs[0].hist(ohis, bins = 256, range = (0, 255))
axs[1].hist(nhis, bins = 256, range = (0, 255))
plt.show()
