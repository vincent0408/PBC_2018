from tkinter import *

import Button as bt

root = Tk()


class App(Frame):
    def __init__(self, master = None, cnf = {}, **kw):
        Frame.__init__(self, master)
        self.grid()
        
        for r in range(6):
            self.master.rowconfigure(r, weight=1)    
        for c in range(5):
            self.master.columnconfigure(c, weight=1)
        return super().__init__(master, cnf, **kw)
        


root.geometry("1024x750")
root.resizable(width = False, height = False)
width = root.winfo_screenwidth() / 2 - 1024/2
height = root.winfo_screenheight() / 2 - 800/2
root.geometry("+%d+%d" % (width, height))


window = App(master=root)

Frame1 = Frame(root, highlightbackground = "black", bg = "white", width = 700, height = 550)
Frame2 = Frame(root, highlightbackground = "black", bg = "red", width = 1024, height = 200)
Frame3 = Frame(root, highlightbackground = "black", bg = "green", width = 324, height = 550)

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

Frame1.grid(row = 0, column = 0, sticky = N+W)
Frame2.grid(row = 1, column = 0, sticky = N+E, columnspan = 2)
Frame3.grid(row = 0, column = 1, sticky = S+E)

Frame2.grid_rowconfigure(0, weight=1)
Frame2.grid_columnconfigure(0, weight=1)

Frame1.grid_propagate("false")
Frame2.grid_propagate("false")
Frame3.grid_propagate("false")



# text box for Frame2
Frame2.grid_rowconfigure(0, weight=1)
Frame2.grid_columnconfigure(0, weight=1)
txt = Text(Frame2, bg = "yellow", font  = ("Microsoft Jhenghe", 20), wrap = WORD)
txt.grid(sticky = W+S+N)
 
# button 
next_button = Button(Frame2, text = "Next", font = ("Microsoft Jhenghe", 20))
next_button.grid(row = 0, column = 1, sticky = N+E+S)


# scrollbar for Frame2
scroll = Scrollbar(Frame2, command = txt.yview)
scroll.grid(row = 0, column = 0, sticky = E+S+N)

# label for Frame1, Frame 3
lbl1 = Label(Frame1, bg = "orange", width = 700, height = 550)
lbl1.grid(sticky = W+S+N+E)
lbl3 = Label(Frame3, bg = "blue", width = 324, height = 550)
lbl3.grid(sticky = W+S+N+E)
img = PhotoImage(file = "./pics/city.gif")
lbl1["image"] = img


# scrollbar finished
txt["yscrollcommand"] = scroll.set

# button command
event_controller = bt.Event()
next_button["command"] = lambda: bt.Event.conbined_function([txt, lbl1, lbl3])










window.mainloop()


