import tkinter
from Canv import *

def main():
	window = tkinter.Tk()
	window.geometry("1920x1080")
	window.title("DIP HW1")
	canv = Canv(window)
	menubar = tkinter.Menu(window)
	
	filemenu = tkinter.Menu(menubar)
	filemenu.add_command(label = "Open", command = lambda: canv.Open())
	filemenu.add_command(label = "Save", command = lambda: canv.Save())
	filemenu.add_command(label = "SaveAs", command = lambda: canv.SaveAs())
	
	editmenu = tkinter.Menu(menubar)
	
	chctrmenu = tkinter.Menu(editmenu)
	chctrmenu.add_command(label = "linear", command = lambda: canv.chctrLINEAR())
	chctrmenu.add_command(label = "exponentially", command = lambda: canv.chctrEXPON())
	chctrmenu.add_command(label = "logarithmically", command = lambda: canv.chctrLOG())
	
	editmenu.add_cascade(label = "change constrast", menu = chctrmenu)

	editmenu.add_command(label = "rotate", command = lambda: canv.rotate())
	editmenu.add_command(label = "resize", command = lambda: canv.resize())
	editmenu.add_command(label = "gray-level slicing", command = lambda: canv.grayhhlight())
	editmenu.add_command(label = "negative", command = lambda: canv.negative())
	editmenu.add_command(label = "auto-level", command = lambda: canv.auto_level())
	editmenu.add_command(label = "bit slicing", command = lambda: canv.bit_slicing())
	editmenu.add_command(label = "smooth", command = lambda: canv.average_filter())
	editmenu.add_command(label = "sharpen", command = lambda: canv.sharpen_filter())
	editmenu.add_command(label = "median filter", command = lambda: canv.median_filter())
	editmenu.add_command(label = "Laplacian filter", command = lambda: canv.Laplacian_filter())
	
	menubar.add_cascade(label = "File", menu = filemenu)
	menubar.add_cascade(label = "Edit", menu = editmenu)

	window['menu'] = menubar
	
	window.mainloop()

if __name__ == "__main__":
	main()
