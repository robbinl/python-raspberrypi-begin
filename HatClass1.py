# 2019 Robbin Law
try:
	from sense_hat import SenseHat
	print("sense_hat.py IS loaded on this machine")
except:
	print("sense_hat.py ISNOT loaded on this machine")

class SenseHatClass():	
	def __init__(self):
		try:
			print("Instantiating SenseHatClass")
			self.hat = SenseHat()
		except:
			print("Unable to Instantiate SenseHatClass")
	def clearHat(self):
		try:
			print("Clearing Sense Hat")
			self.hat.clear()
		except:
			print("Unable to Clear Sense Hat")
	
	def getTemp(self):
		try:
			print("Sensing Real SenseHat Temperature")
			temp = self.hat.get_temperature()
			if temp is None:
				raise Exception("Temperature is NONE")
			else:
				temp = round(temp, 2)
				return temp
		except Exception as e:
			print(e)
			print("Temperature Data Not Available")
			return 0
	
	def getHum(self):
		try:
			print("Sensing Real SenseHat Humidity")
			hum = self.hat.get_humidity()
			if hum is None:
				raise Exception("Humidity is NONE")
			else:
				hum = round(hum, 2)
				return hum
		except Exception as e:
			print(e)
			print("Humidity Data Not Available")
			return 0				
				
