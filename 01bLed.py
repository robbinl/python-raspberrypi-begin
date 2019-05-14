# 2019 Robbin Law
import time
try:
	from sense_hat import SenseHat
	print("sense_hat IS loaded on this machine")
except:
	print("sense_hat ISNOT loaded on this machine")

r = 255
g = 0
b = 0

def next_colour():
    global r
    global g
    global b

    if (r == 255 and g < 255 and b == 0):
        g += 1
    if (g == 255 and r > 0 and b == 0):
        r -= 1
    if (g == 255 and b < 255 and r == 0):
        b += 1
    if (b == 255 and g > 0 and r == 0):
        g -= 1
    if (b == 255 and r < 255 and g == 0):
        r += 1
    if (r == 255 and b > 0 and g == 0):
        b -= 1

def main():
    hat = SenseHat()   
    while True:
        try:
            hat.clear([r, g, b])
            x = 2/1000
            time.sleep(x)
            next_colour()
        except KeyboardInterrupt as ki:
            print("Caught:", repr(ki))
            print("Exiting.")
            hat.clear()
            break

main()