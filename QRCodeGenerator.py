from tkinter import Tk, PhotoImage, filedialog, ttk
Label = ttk.Label
Entry = ttk.Entry
Button = ttk.Button

import qrcode




class Application :
	def __init__ (self) :
		self.root = Tk()
		self.root.title('QR Code generator | v1.0')
		self.root.iconphoto(0, PhotoImage(file='icon.png'))
		self.root.resizable(0, 0)

		self.root.tk.call('source', 'theme.tcl')
		self.root.tk.call('set_theme', 'light')


	def generate (self) :
		if self.text.get() :
			img = qrcode.make(self.text.get())
			if self.filename.get() :
				path = filedialog.askdirectory(title='Select folder')
				print(path)
				img.save(path + '\\' + self.filename.get() + '.png')
			else :
				img.save('qrcode.png')


	def start (self) :
		Label(self.root, text='Text:').grid(row=0, column=0, padx=10, pady=10)
		Label(self.root, text='File name:').grid(row=1, column=0, padx=10, pady=10)

		Label(self.root, text='.png').grid(row=1, column=2, padx=10, pady=10)

		self.text = Entry(self.root, width=38)
		self.text.grid(row=0, column=1, columnspan=2, padx=10, pady=10)

		self.filename = Entry(self.root, width=30)
		self.filename.grid(row=1, column=1, padx=10, pady=10)

		Button(self.root, text='Generate', command=self.generate).grid(row=2, column=0, columnspan=3, padx=10, pady=10)


		self.root.mainloop()
		


if __name__ == '__main__' :
	Application().start()