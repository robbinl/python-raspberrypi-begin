def spam(divideBy):
    return 42/divideBy

try:
    print("begin of try")
    print(spam(2))
    print (spam(12))
    #print (spam(0))
    print (spam(1))
    #raise Exception("We set this one")
    print("end of try")
except ZeroDivisionError:
    print("Divide by Zero error")
except Exception as e:
	print(e)
except:
    print("last except")
finally:
    print("our final step that happens every time")
	
    
