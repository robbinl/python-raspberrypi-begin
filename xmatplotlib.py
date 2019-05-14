#import matplotlib.pyplot as plt
from time import sleep
from sense_hat import SenseHat
import tkinter as Tk

#import tkFont
from tkinter import font

sense = SenseHat()

plt.ion()	# turn on interactive plotting

class RPiSenseHat(Tk.Frame):
	
	def __init__(self, master):
		self.master = master
        		
		# Background : Dark : 0 / White : 1
		self.background = 0
		self.startGUI()
		self.running = False
		
	def startGUI(self):
		self.master.title("RPi SenseHat")
		self.master.grid_rowconfigure(1, weight=1)
		self.master.grid_columnconfigure(1, weight=1)
		
		self.frame = Tk.Frame(self.master)
		self.frame.pack(fill=Tk.X, padx=5, pady=5)
		
		# Setting font size and type
#		helv12 = tkFont.Font(family='Helvetica', size=12, weight='bold') 
		helv12 = font.Font(family='Helvetica', size=12, weight='bold') 

		# Button : Temperature Sensor
		self.button1 = Tk.Button(self.frame, bg = 'white', text="Temperature", height = 2, width = 20,
			command = self.senseTemperature, font=helv12)
		self.button1.pack()

		# Button : Pressure Sensor
		self.button2 = Tk.Button(self.frame, bg = 'white', text="Pressure", height = 2, width = 20,
			command = self.sensePressure, font=helv12)
		self.button2.pack()

		# Button : Humidity Sensor
		self.button3 = Tk.Button(self.frame, bg = 'white', text="Humidity", height = 2, width = 20,
			command = self.senseHumidity, font=helv12)
		self.button3.pack()


		# Button : Record
		self.button4 = Tk.Button(self.frame, bg = 'white', text="Recording", height = 2, width = 20,
			command = self.recording, font=helv12)
		self.button4.pack()
		

	def senseTemperature(self):
		""" Senses Current Temperature """
		print ("Sensing Temperature")
		temp = sense.get_temperature()
		self.button1["bg"] = 'orange'
		self.button1["text"] = 'Temperature \n' + str("%.3f" %temp) + ' deg. C'

	def sensePressure(self):
		""" Senses Current Pressure """
		print ("Sensing Pressure")
		pres = sense.get_pressure()
		self.button2["bg"] = 'orange'
		self.button2["text"] = 'Pressure \n' + str("%.3f" %pres) + ' hPa '

	def senseHumidity(self):
		""" Senses Current Humidity """
		print ("Sensing Humidity")
		humi = sense.get_humidity()
		self.button3["bg"] = 'orange'
		self.button3["text"] = 'Humidity \n' + str("%.3f" %humi) + ' (%) '
		
	def recording(self):
            
                pressure_list = []
                temp_list = []
                humidity_list = []
                x = []
                plt.show()
                
                while True:
                    
                    for a in range(20):
                        
                        pressure = sense.get_pressure() / 1000
                        pressure_list.append(pressure)
                        
                        temp = sense.get_temperature() / 10
                        temp_list.append(temp)
                        
                        humidity = sense.get_humidity() / 10
                        humidity_list.append(humidity)
                        
                        print(pressure, temp, humidity)
                        
                        x.append(a)
                        
                        #sleep(2)
                        
                    plt.figure().clf()
                    plt.plot(x,humidity_list)
                    plt.plot(x,temp_list,'r')
                    plt.plot(x,pressure_list,'g')
                    plt.draw()
                    

if __name__ == "__main__":
	
	root = Tk.Tk()
	app = RPiSenseHat(root) 
	root.mainloop()
	

