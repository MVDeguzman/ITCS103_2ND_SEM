import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def show_graph():
    # Sample data
    categories = ['1A', '1B', '1C']
    values = [120, 250, 70]

    # Create Tkinter window
    root = tk.Tk()
    root.title("Tkinter Bar Graph")
    root.geometry("500x400")

    # Create bar chart
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['blue', 'green', 'red'])
    ax.set_title("Macronutrient Breakdown")
    ax.set_ylabel("Grams")

    # Embed chart in Tkinter
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()

    root.mainloop()

def line_graph():
    # Sample data
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







# Run it
show_graph()
