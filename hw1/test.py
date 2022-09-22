from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
from chctr import *
from rotate import *
from resize import *
from grayslice import *
from negative import *

def main():
	window = tkinter.Tk()
	window.geometry("1920x1080")
	window.title("DIP HW1")

	canvas = tkinter.Canvas(window, width = 1000, height = 1000)
	img = Image.open("./testdata/woman.tif")
	#img.show()
	photo = ImageTk.PhotoImage(img)
	canvas.create_image(400, 400, anchor = tkinter.CENTER, image = photo)
	canvas.pack()
	
	#new = chctrLINEAR(img, 1, -50)
	#new = chctrEXPON(img, 0.1, 1)
	#new = chctrLOG(img, 1e9, 2)
	#new = rotate(img, 12, expand = True)
	#new = resize(img, 200)
	#new = grayhhlight(img, 50, 100, hhlightV = 200, preserve = True)
	#new = negative(img)

	#img.show()
	#new.show()
	window.mainloop()

if __name__ == "__main__":
	main()
