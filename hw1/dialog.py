import tkinter

class dialog():
	def __init__(self, window, n, labels):
		self.n = n
		self.window = window
		self.top = tkinter.Toplevel(window)
		self.top.geometry("450x250")

		self.entries = []
		self.labels = []
		self.inputs = [None] * n
		for i in range(n):
			self.labels.append(tkinter.Label(self.top, text = labels[i]))
			self.entries.append(tkinter.Entry(self.top))
			self.labels[i].pack()
			self.entries[i].pack()
		btnCF = tkinter.Button(self.top, text = "confirm", command = lambda: self.__confirm())
		btnCF.pack()
		btnCN = tkinter.Button(self.top, text = "cancel", command = lambda: self.__cancel())
		btnCN.pack()

	def __confirm(self):
		for i in range(self.n):
			self.inputs[i] = self.entries[i].get()
		self.top.destroy()

	def __cancel(self):
		self.top.destroy()
