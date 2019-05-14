# 2019 Robbin Law
import time
import datetime
import threading
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
try:
	print("DbClass1.py IS loaded in this directory")
	from DbClass1 import DataBaseClass
except:
	print("DbClass1.py IS NOT loaded in this directory")

class App(tk.Tk):
    dbname = "SensorsData.db"
    tbname = "HatData"
    UpdateTime = 1000
    Status = "Huston we are a go"
    LogDataRecordCount = 0
    event = threading.Event()
    StopThread = 0
        
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("RPi Data Logging and Display")
        self.geometry("1280x720")

        containerFrame = tk.Frame(self)
        containerFrame.pack(side="top", fill="both", expand = True)
        containerFrame.rowconfigure(0, weight=1)
        containerFrame.columnconfigure(0, weight=1)
        
        self.label0 = tk.Label(containerFrame, text='Status = ' + self.Status)
        self.label0.pack(pady=2,padx=10)
        
        self.label1 = tk.Label(containerFrame, text='Update Time = ' + str(self.UpdateTime) + ' ms')
        self.label1.pack(pady=2,padx=10)
        
        timestamp = datetime.datetime.now()
        label2 = tk.Label(containerFrame, text='Time Stamp = ' + str(timestamp))
        label2.pack(pady=2,padx=10)
        
        temp = 3.0
        label3 = tk.Label(containerFrame, text='Temperature = ' + str("%.3f" %temp) + ' degC')
        label3.pack(pady=2,padx=10)
        hum = 4.0
        label4 = tk.Label(containerFrame, text='Humidity = ' + str("%.3f" %hum) + ' %')
        label4.pack(pady=2,padx=10)
        
        menubar = tk.Menu(containerFrame)

        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        dbmenu = tk.Menu(menubar, tearoff=1)
        dbmenu.add_command(label="Start Logging",
            command=lambda: self.logDataStart())
        dbmenu.add_command(label="Stop Logging",
            command=lambda: self.logDataStop())
        menubar.add_cascade(label="Db", menu=dbmenu)
        
        updatetimemenu = tk.Menu(menubar, tearoff=2)
        updatetimemenu.add_command(label="1 sec",
            command=lambda: self.setUpdateTime(1000))
        updatetimemenu.add_command(label="2 sec",
            command=lambda: self.setUpdateTime(2000))
        updatetimemenu.add_command(label="5 sec",
            command=lambda: self.setUpdateTime(5000))
        menubar.add_cascade(label="UpdateTime", menu=updatetimemenu)
        tk.Tk.config(self, menu=menubar)
        t1 = threading.Thread(target = self.Operation)
        t1.daemon = True
        t1.start()

    def setUpdateTime(self, time):
        self.UpdateTime = time
        self.label1["text"] = "New Update Time = " + str(self.UpdateTime) + " ms"
    
    def logDataStart(self):
        #self.label0["text"] = "New Status = Start Logging Data"
        #self.LogDataFlag = 1
        self.event.set()
    
    def logDataStop(self):
        #self.label0["text"] = "New Status = Stop Logging Data"
        #self.LogDataFlag = 0
        self.event.clear()
    
    def Operation(self):
        while True:
            self. event.wait()
            self.LogDataRecordCount += 1
            print("Hey I am running")
            self.label0["text"] = "New Status = Records Logged Count = " +str(self.LogDataRecordCount)
            time.sleep(1)

#event = threading.Event()
#t1 = threading.Thread(target = control)
#t2 = threading.Thread(target = Operation)
#t1.start()
#t2.start()
#t1.join()

#testApp = DataBaseClass()
#testApp.createDataBase(dbname)
#testApp.createTable(dbname, tbname)
#testApp.logData(dbname, tbname, 2.0, 3.0)
#rows = testApp.retrieveData(dbname, tbname, "1")
#for row in rows:
#    print ("TimeStamp = "+str(row[0])+" ==> Temp = "+str(row[1])+"	Hum = "+str(row[2]))

app = App()
app.mainloop()
