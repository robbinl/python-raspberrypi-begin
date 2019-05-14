# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk	
try:
	print("senseHatClass1.py IS loaded in this directory")
	from HatClass1 import SenseHatClass
except:
	print("senseHatClass1.py IS NOT loaded in this directory")

class App(tk.Tk):	
	def __init__(self):
		tk.Tk.__init__(self)
		self.title("RPi SenseHat and Tk OOP")
		self.geometry("400x200")
		self.grid_rowconfigure(1, weight=1)
		self.grid_columnconfigure(1, weight=1)
		self.frame = tk.Frame(self)
		self.frame.pack(side="top", fill="both", expand = True)
		self.label = tk.Label(self.frame, text="Page One: Press Buttons to see real data")
		self.label.pack(pady=10,padx=10)
		self.button1 = tk.Button(self.frame, bg = 'white', text="Temperature", height = 2, width = 20,
			command = self.senseTemperature)
		self.button1.pack()
		self.button2 = tk.Button(self.frame, bg = 'white', text="Humidity", height = 2, width = 20,
			command = self.senseHumidity)
		self.button2.pack()
		self.senseHat = SenseHatClass()		
	def senseTemperature(self):
		temp = self.senseHat.getTemp()
		self.button1["text"] = 'Temperature \n' + str("%.3f" %temp) + ' degC'
	def senseHumidity(self):
		hum = self.senseHat.getHum()
		self.button2["text"] = 'Humidity \n' + str("%.3f" %hum) + ' %'
				
app = App() 
app.mainloop()				
