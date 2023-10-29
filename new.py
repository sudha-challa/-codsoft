import tkinter as tk
from tkinter.ttk import *

# Create the main window
root = tk.Tk()

# Set the window title
root.title("Centered Window")

# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the width and height of the window
window_width = 400
window_height = 300

# Calculate the x and y coordinates to center the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the geometry of the window to center it on the screen
root.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Run the main loop
root.mainloop()




