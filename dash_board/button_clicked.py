import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def show_bar_graph():
    # Data
    categories = ['Protein', 'Carbs', 'Fats']
    values = [120, 250, 70]

    # Create a new window for graph
    graph_window = tk.Toplevel(root)
    graph_window.title("Bar Graph")
    graph_window.geometry("500x400")

    # Create the figure
    fig, ax = plt.subplots()
    ax.bar(categories, values, color=['blue', 'green', 'red'])
    ax.set_title("Macronutrient Breakdown")
    ax.set_ylabel("Grams")

    # Embed the graph into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=graph_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

# Main window
root = tk.Tk()
root.title("Dashboard")
root.geometry("300x200")

# Button to show graph
graph_button = tk.Button(root, text="Show Bar Graph", command=show_bar_graph)
graph_button.pack(pady=20)

root.mainloop()
