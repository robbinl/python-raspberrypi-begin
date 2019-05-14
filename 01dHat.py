# 2019 Robbin Law
import time
try:
	from sense_hat import SenseHat
	print("sense_hat IS loaded on this machine")
except:
	print("sense_hat ISNOT loaded on this machine")

samplefreq = 1 # time in seconds

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
	
def getDataandPrint(hat):
    temp = getTemp(hat)
    print("Temperature is", temp, "degC")
    hum = getHum(hat)
    print("Humidity is", hum, "%")

def main():
    hat = SenseHat()
    clearHat(hat)    
    while True:
        try:
            getDataandPrint(hat)
            time.sleep(samplefreq)
        except KeyboardInterrupt as ki:
            print("Caught:", repr(ki))
            print("Exiting.")
            break

main()

