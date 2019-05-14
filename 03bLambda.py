# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk

def func0():
	print("This worked but not passing any params")

def func1(p):
	print(p)

def main():
	win = tk.Tk()
	win.title("Using LAMBDA")
	win.geometry("400x200")
	win.grid_rowconfigure(1, weight=1)
	win.grid_columnconfigure(1, weight=1)
	frame = tk.Frame(win)
	frame.pack(side="top", fill="both", expand = True)
	label = tk.Label(frame, text="Page One: Press Button to see how LAMBDA works")
	label.pack(pady=10,padx=10)
	button1 = tk.Button(frame, bg = 'white', text="Test Lambda", height = 2, width = 20, command = func0)
	#button1 = tk.Button(frame, bg = 'white', text="Test Lambda", height = 2, width = 20, command = func1("Is this going to work"))
	#button1 = tk.Button(frame, bg = 'white', text="Test Lambda", height = 2, width = 20, command = lambda: func1("Yes this worked"))
	button1.pack()
	win.mainloop()

main()