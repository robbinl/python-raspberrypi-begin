# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk
try:
	from sense_hat import SenseHat
	print("sense_hat IS loaded on this machine")
except:
	print("sense_hat ISNOT loaded on this machine")

def clearHat(hat):
	try:
		print("Clearing Sense Hat")
		hat.clear()
	except:
		print("Unable to Clear Sense Hat")
	
def getTemp(hat):
	try:
		print("Sensing Real SenseHat Temperature")
		temp = hat.get_temperature()
		if temp is None:
			raise Exception("Temperature is NONE")
		else:
			temp = round(temp, 2)
			return temp
	except Exception as e:
		print(e)
		print("Temperature Data Not Available")
		return 0
	
def getHum(hat):
	try:
		print("Sensing Real SenseHat Humidity")
		hum = hat.get_humidity()
		if hum is None:
			raise Exception("Humidity is NONE")
		else:
			hum = round(hum, 2)
			return hum
	except Exception as e:
		print(e)
		print("Humidity Data Not Available")
		return 0				

def senseTemperature(hat, button1):
	temp = getTemp(hat)
	button1["text"] = 'Temperature \n' + str("%.3f" %temp) + ' degC'
	
def senseHumidity(hat, button2):
	hum = getHum(hat)
	button2["text"] = 'Humidity \n' + str("%.3f" %hum) + ' %'
		
def main():
	hat = SenseHat()
	clearHat(hat)
	win = tk.Tk()
	win.title("RPi SenseHat and Tk but no OOP")
	win.geometry("400x200")
	win.grid_rowconfigure(1, weight=1)
	win.grid_columnconfigure(1, weight=1)
	frame = tk.Frame(win)
	frame.pack(side="top", fill="both", expand = True)
	label = tk.Label(frame, text="Page One: Press Buttons to see real data")
	label.pack(pady=10,padx=10)
	button1 = tk.Button(frame, bg = 'white', text="Temperature", height = 2, width = 20,
		command = lambda: senseTemperature(hat, button1))
	button1.pack()
	button2 = tk.Button(frame, bg = 'white', text="Humidity", height = 2, width = 20,
		command = lambda: senseHumidity(hat, button2))
	button2.pack()
	win.mainloop()

main()