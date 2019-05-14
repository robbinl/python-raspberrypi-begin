# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk	

class App():	
	def __init__(self, master):
		master.title("Tk OOP with no Inheritance")
		master.geometry("400x200")
		master.grid_rowconfigure(1, weight=1)
		master.grid_columnconfigure(1, weight=1)
		self.frame = tk.Frame(master)
		self.frame.pack(side="top", fill="both", expand = True)
		self.label = tk.Label(self.frame, text="Page One: Hello with OOP but no Inheritance")
		self.label.pack(pady=10,padx=10)
		print("self is of type " +str(type(self)))
		print("master is of type " +str(type(master)))
		print("self.frame is of type " +str(type(self.frame)))
		print("self.label is of type " +str(type(self.label)))
	

win = tk.Tk()				
app = App(win) 
win.mainloop()				
