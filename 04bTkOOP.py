# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk	

class App(tk.Frame):	
	def __init__(self, master=None):
		tk.Frame.__init__(self, master)
		self.pack(side="top", fill="both", expand = True)
		self.label = tk.Label(self, text="Page One: Hello with OOP and Frame Inheritance")
		self.label.pack(pady=10,padx=10)
		print("self is of type " +str(type(self)))
		print("master is of type " +str(type(master)))
		#print("self.frame is of type " +str(type(self.frame)))
		print("self.label is of type " +str(type(self.label)))
	
				
app = App()
app.master.title("Tk OOP with Frame Inheritance")
app.master.geometry("400x200")
app.master.grid_rowconfigure(1, weight=1)
app.master.grid_columnconfigure(1, weight=1)		 
app.mainloop()				
