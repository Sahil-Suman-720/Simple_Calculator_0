from tkinter import *
from datetime import *
i = 1
while i<=10:
    root = Tk()
    root.geometry('1280x720')
    root.configure(bg = '#025091')
    var = datetime.now().strftime("%H:%M:%S")
    lb0 = Label(root,text = "THE CURRENT TIME IS"
        ,font = ("Bahnschrift",30,'bold'),fg = "#71C5EE",bg = "#025091")
    lb = Label(root,text = var
        ,font = ("Bahnschrift",100,'bold'),fg = "#71C5EE",bg = "#025091")
    lb0.place(x = 430,y = 200)
    lb.pack(padx = 390,pady = 250)
    def myfun1():
        root.destroy()
    root.after(1000,lambda:myfun1())
    i += 1
    root.mainloop()