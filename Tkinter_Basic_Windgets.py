from tkinter import *
import tkinter as tk


main = tk.Tk()
main.title("TEST PROJECT")
main.geometry("900x900")

"""Label"""
label = tk.Label(master= main, text= "Wala Nang Peraaaa", font=("Times New Roman", 20))
label.pack()

"""Button"""
button = tk.Button(master= main, text= "A Button", command= main.destroy)
button.pack()

"""Entry"""

entry = tk.Entry(main)
entry.pack()

"""Frame"""
frame = tk.Frame(main, width= 20, height= 20, borderwidth= 10, 
                  relief= tk.GROOVE)
frame.propagate(False)
frame.pack()

"""CheckButton"""
var1 = IntVar()
ck = tk.Checkbutton(main, text= "hellooo", variable= var1)
ck.pack()

var2 = IntVar()
ck2 = tk.Checkbutton(main, text= "hiiii", variable= var2)
ck2.pack()

"""RadioButton"""
sex = IntVar()
rb1 = tk.Radiobutton(main, text= "Male", value= sex)
rb1.pack()

rb2 = tk.Radiobutton(main, text= "Female", value= sex)
rb2.pack()

"""List Box"""
lb = tk.Listbox(main)
lb.insert(1, "Hello")
lb.insert(2, "Hi")
lb.insert(3, "Halow")
lb.insert(4, "Ayoo")
lb.insert(5, "Bye")
lb.pack()

"""Scroll Bar"""
sb = tk.Scrollbar(main)
sb.pack(side=RIGHT, fill= Y)

mylist = tk.Listbox(main, yscrollcommand=Scrollbar.set)

for i in range(100):
    mylist.insert(END, "This is line number" + str(i))

mylist.pack(side=LEFT, fill=BOTH)
sb.config(command=mylist.yview)

"""Menu"""
menu = tk.Menu(main)
main.config(menu=menu)

filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New")
filemenu.add_command(label="Open")
filemenu.add_separator()
filemenu.add_command(label="Delete")

helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About")

"""Canvas"""
canvas = tk.Canvas(main, width= 25, height= 55)
canvas.pack()

canvas_h = 20
canvas_w = 200
y = int(canvas_h / 2)

canvas.create_line(0, y, canvas_w, y)

main.mainloop()