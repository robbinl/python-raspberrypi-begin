# 2019 Robbin Law
try:
	from sense_hat import SenseHat
	print("sense_hat IS loaded on this machine")
except:
	print("sense_hat ISNOT loaded on this machine")

def main():
    hat = SenseHat()
    hat.clear()   
    while True:
        try:
            hat.set_rotation(180)
            red = (255, 0, 0)
            hat.show_message("Hello World", text_colour=red)
        except KeyboardInterrupt as ki:
            print("Caught:", repr(ki))
            print("Exiting.")
            hat.clear()
            break

main()