# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk	

class App(tk.Tk):
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("Tk OOP with Tk Inheritance")
		self.geometry("400x200")
		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.frame = tk.Frame(self)
		self.frame.pack(side="top", fill="both", expand = True)
		self.label = tk.Label(self.frame, text="Page One: Hello with OOP and TK Inheritance")
		self.label.pack(pady=10,padx=10)
		print("self is of type " +str(type(self)))
		#print("master is of type " +str(type(master)))
		print("self.frame is of type " +str(type(self.frame)))
		print("self.label is of type " +str(type(self.label)))
	
				
app = App() 
app.mainloop()				
