
import tkinter as tk
from tkinter import *


# creating main tkinter window/toplevel
master = tk.LabelFrame()


label= Label(master, text="Enrollment Form", font=("Arial", 20, "bold"), fg="black")
label.grid(row=0, column=10, pady=40)

# this will create a label widget and grid method to arrange labels in respective,  rows and columns as specified

#for stud name
l1 = Label(master, text =" Students Name:").grid(row = 3, column = 5, sticky = W, pady = 4, padx = 10)
first= Label(master, text="First Name:").grid(row = 5, column = 5, sticky = W, pady = 0, padx = 10)
last= Label(master, text="Last Name:").grid(row = 5, column = 6, sticky = W, pady = 0, padx = 10)

# for age
l2 = Label(master, text="Date of birth:").grid(row = 7, column = 5, sticky = W, pady = 4, padx = 10)
# date= Label(master, text="Date").grid(row = 7, column = 7, sticky = W,)


# entry widgets, used to take entry from user and this will arrange entry widgets

# entry for stud name
e1 = Entry(master,bg="lightblue").grid(row = 4, column = 5, sticky = W, pady = 4, padx = 10)
e11= Entry(master, bg="lightblue").grid(row = 4, column = 6, sticky = W, pady = 4, padx = 10)

# entry for age
e2 = Entry(master, bg="lightblue").grid(row = 8, column = 5, sticky = W, padx = 10)


# infinite loop which can be terminated by keyboard
# or mouse interrupt
mainloop()