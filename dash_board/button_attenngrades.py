import tkinter as tk
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

window = tk.Tk()
window.title("Attendance Grades")
window.geometry('600x600')
window.configure(bg="white")

main_frame = tk.Frame(window, bg="white")
main_frame.place(relx=0.5, rely=0.5, anchor="center")


frame_attendance = tk.Frame(main_frame, bg="bisque3")
frame_attendance.pack()
frame_grades = tk.Frame(main_frame, bg="bisque3")
frame_grades.pack(pady=50)

frame_grades



def newwindow():
    # Create a new window

    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry('300x200')
    
    label = tk.Button(new_window, text="attendance", font=("Arial", 15))
    label.pack(pady=20)

def newwindow1():
    # Create a new window

    new_window = tk.Toplevel(window)
    new_window.title("New Window")
    new_window.geometry('300x200')
    
    label = tk.Button(new_window, text="grades 2nd sem", font=("Arial", 15), command = clicked_linegraph)
    label.pack(pady=20)

    label1 = tk.Button(new_window, text="grades 1st sem", font=("Arial", 15), command = clicked_linegraph)
    label1.pack(pady=20)



def destroy():
    main_frame.destroy()


def clicked_linegraph():
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    # Create Tkinter window
    root = tk.Tk()
    root.title("Tkinter Line Graph")
    root.geometry("500x400")

    # Create line chart
    fig, ax = plt.subplots()
    ax.plot(x, y, marker='o')
    ax.set_title("Sample Line Graph")
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    # Embed chart in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()



attendance_button= tk.Button(frame_attendance, text="Attendace", font=("Arial", 15), bg= "dodgerblue2", fg= "white", width= 33, command=newwindow)
attendance_button.grid(row=0, column=2, padx=10, pady=10)

grade_button= tk.Button(frame_grades, text="Grades", font=("Arial", 15), bg= "dodgerblue2", fg= "white", width= 33, command=newwindow1)
grade_button.grid(row=1, column=2, padx=10, pady=10)

back_button = tk.Button(window, text="Back", font=("Arial", 15), bg= "dodgerblue2", fg= "white", command=window.destroy)
back_button.place(relx=0.8, rely=0.1, anchor="nw")

window.mainloop()