# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk

def main():
	win = tk.Tk()
	win.title("Tk no OOP")
	win.geometry("400x200")
	win.grid_rowconfigure(1, weight=1)
	win.grid_columnconfigure(1, weight=1)
	frame = tk.Frame(win)
	frame.pack(side="top", fill="both", expand = True)
	label = tk.Label(frame, text="Page One: Hello with no OOP")
	label.pack(pady=10,padx=10)
	print("win is of type " +str(type(win)))
	print("frame is of type " +str(type(frame)))
	print("label is of type " +str(type(label)))
	win.mainloop()

main()