# 2019 Robbin Law
try:
	print("importing tkinter from Python 3.X")
	import tkinter as tk
	from tkinter import ttk	 
except:
	print("importing tkinter from Python 2.X")
	import Tkinter as tk	

FONT=("TimesNewRoman", 10)

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Tk with Menu and Pages")
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
        tk.Tk.config(self, menu=menubar)

        self.pages = {}
        for page in (PageOne, PageTwo, PageThree):
            newPage = page(containerFrame, self)
            self.pages[page] = newPage 
            newPage.grid(row=0, column=0, sticky="nsew")
        self.showPage(PageOne)

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
