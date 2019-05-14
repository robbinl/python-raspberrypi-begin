# 2019 Robbin Law
import datetime as dt

import tkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style

FONT=("TimesNewRoman", 10)

class App(tk.Tk):
    UpdateTime = 1000
    x = []
    xlabel = []
    y0 = []
    y1 = []   
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("RPi Full Project")
        self.geometry("1280x720")

        containerFrame = tk.Frame(self)
        containerFrame.pack(side="top", fill="both", expand = True)
        containerFrame.rowconfigure(0, weight=1)
        containerFrame.columnconfigure(0, weight=1)

        menubar = tk.Menu(containerFrame)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings", 
            command=lambda: self.popupmsg("Not supported yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        updateTimeChoice = tk.Menu(menubar, tearoff=1)
        updateTimeChoice.add_command(label="1 sec",
            command=lambda: self.setUpdateTime(1000))
        updateTimeChoice.add_command(label="2 sec",
            command=lambda: self.setUpdateTime(2000))
        updateTimeChoice.add_command(label="5 sec",
            command=lambda: self.setUpdateTime(5000))
        menubar.add_cascade(label="UpdateTime", menu=updateTimeChoice)
        tk.Tk.config(self, menu=menubar)

        self.pages = {}
        for page in (PageOne, PageTwo, PageThree):
            newPage = page(containerFrame, self)
            self.pages[page] = newPage 
            newPage.grid(row=0, column=0, sticky="nsew")
        self.showPage(PageOne)
        self.fig = Figure(figsize=(14, 6), dpi=100)
        self.canvas = FigureCanvasTkAgg(self.fig, self.pages[PageTwo])
        self.buildNewCharts()

    def animate(self, i, axis0, axis1):
        tempx = i
        tempy = i
        self.x.append(tempx)
        self.xlabel.append(dt.datetime.today().strftime("%H:%M:%S"))
        self.y0.append(tempy)
        self.y1.append(tempy)
        self.x = self.x[-10:]
        self.xlabel = self.xlabel[-10:]
        self.y0 = self.y0[-10:]
        self.y1 = self.y1[-10:]
        axis0.clear()
        axis0.plot(self.x, self.y0)
        axis1.clear()
        axis1.plot(self.x, self.y1)
        axis0.set_title("hey")
        axis0.set_xlabel('Time in HH:MM:SS')
        axis0.set_ylabel('Temperature in degC')
        axis0.set_xticklabels(self.xlabel)
        for tick in axis0.get_xticklabels():
            tick.set_rotation(90)
            tick.set_fontsize(8)
        for tick in axis0.get_yticklabels():
            tick.set_fontsize(8)

    def showPage(self, pagename):
        pagetoShow = self.pages[pagename]
        pagetoShow.tkraise()

    def popupmsg(self, msg):
        popup = tk.Tk()
        popup.wm_title("Popup")
        label1 = ttk.Label(popup, text=msg, font=FONT)
        label1.pack(side="top", fill="x", pady=10)
        button1 = ttk.Button(popup, text="Okay", command = popup.destroy)
        button1.pack()
        popup.mainloop()

    def setUpdateTime(self, time):
        self.UpdateTime = time
        self.buildNewCharts()

    def buildNewCharts(self):
        self.canvas.get_tk_widget().destroy()
        fig = Figure(figsize=(14, 6), dpi=100)
        axis0 = fig.add_subplot(121)    # 1 row, 2 columns, 1st graph
        axis1 = fig.add_subplot(122)    # 1 row, 2 columns, 2nd graph       
        fig.subplots_adjust(bottom=0.30)
        self.canvas = FigureCanvasTkAgg(fig, self.pages[PageTwo])
        ani = animation.FuncAnimation(fig, self.animate, fargs=(axis0, axis1), interval=self.UpdateTime)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side="top", fill="both", expand=1)
               
class PageOne(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        label = tk.Label(self, text="Page One", font=FONT)
        label.pack(pady=10,padx=10)
        button = ttk.Button(self, text="Go to Page Two",
            command=lambda: controller.showPage(PageTwo))
        button.pack()
        button2 = ttk.Button(self, text="Go to Page Three",
            command=lambda: controller.showPage(PageThree))
        button2.pack()

class PageTwo(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        label = ttk.Label(self, text="Page Two", font=FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Go to Page One",
            command=lambda: controller.showPage(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Go to Page Three",
            command=lambda: controller.showPage(PageThree))
        button2.pack()
        
class PageThree(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        label = ttk.Label(self, text="Page Three", font=FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Go to Page One",
            command=lambda: controller.showPage(PageOne))
        button1.pack()
        button2 = ttk.Button(self, text="Go to Page Two",
            command=lambda: controller.showPage(PageTwo))
        button2.pack()
              
app = App()
app.mainloop()
