import tkinter as tk
from tkinter import*
from tkinter import messagebox
from openpyxl import Workbook
from openpyxl import load_workbook


def create_excel_file():
    wb = Workbook()
    ws = wb.active
    ws.title = "UserData"
    ws.append(["Name", "Score", "Remarks"])
    wb.save("userdata.xlsx")



window = tk.Tk()
window.title("possible")
window.geometry("800x400")

mainframe= tk.Frame(window)
mainframe.pack()
secframe= tk.LabelFrame(mainframe)

secframe.pack()

title= tk.Label(secframe, text= "INFORMATION")
title.grid(row=0, column=2)

grade_label= tk.Label(secframe, text= "grade")
grade_label.grid(row=1, column=1, pady=5, padx=5)

grade_entry= tk.Entry(secframe)
grade_entry.grid(row=1, column=2, pady=5, padx=5)

sub_label= tk.Label(secframe, text= "subject")
sub_label.grid(row=2, column=1, pady= 5,padx=5)

sub_entry= tk.Entry(secframe)
sub_entry.grid(row=2, column=2, pady=5, padx=5)


enter_Button= tk.Button(secframe, text= "ENTER")
enter_Button.grid(row=3, column=1, pady= 10,padx=10)

update_Button= tk.Button(secframe, text= "UPDATE")
update_Button.grid(row=3, column=2, pady= 10,padx=10)


window.mainloop()