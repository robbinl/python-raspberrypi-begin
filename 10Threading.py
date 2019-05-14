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

class App(tk.Tk):
    Status = "Huston we are a go"
    LogDataRecordCount = 0
    event = threading.Event()
    StopThread = 0
        
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Threading")
        self.geometry("1280x720")

        containerFrame = tk.Frame(self)
        containerFrame.pack(side="top", fill="both", expand = True)
        containerFrame.rowconfigure(0, weight=1)
        containerFrame.columnconfigure(0, weight=1)
        
        self.label0 = tk.Label(containerFrame, text='Status = ' + self.Status)
        self.label0.pack(pady=2,padx=10)
        
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
        
        tk.Tk.config(self, menu=menubar)
        
        t1 = threading.Thread(target = self.Operation)
        t1.daemon = True
        t1.start()

    def logDataStart(self):
        self.event.set()
    
    def logDataStop(self):
        self.event.clear()
    
    def Operation(self):
        while True:
            self. event.wait()
            self.LogDataRecordCount += 1
            print("Hey I am running")
            self.label0["text"] = "New Status = Records Logged Count = " +str(self.LogDataRecordCount)
            time.sleep(1)

app = App()
app.mainloop()
