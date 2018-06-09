from tkinter import *


def create_window(s1, s2, txt):
    opt = [s1, s2]
    root = Tk()
    root.title("問題")
    
    frame = Frame(root)
    lbl = Label(frame, text = txt, font = ("Microsoft Jhenghe", 18), bg = "orange")
    frame.pack(fill = "both", expand = "true")
    lbl.pack(fill = "both", expand = "true")

    bttn1 = Button(frame, text = opt[0], font = ("Microsoft Jhenghe", 18))
    bttn2 = Button(frame, text = opt[1], font = ("Microsoft Jhenghe", 18))
    quit(root, bttn1, bttn2)
    bttn1.pack(side = "left", fill = "x", expand = "true")
    bttn2.pack(side = "left", fill = "x", expand = "true")

    width = root.winfo_screenwidth() / 2 - root.winfo_reqwidth()
    height = root.winfo_screenheight() / 2 - root.winfo_reqheight()
    root.geometry("+%d+%d" % (width, height))

    root.mainloop()
    

def quit(root, bttn1, bttn2):
    bttn1["command"] = root.destroy
    bttn2["command"] = root.destroy


