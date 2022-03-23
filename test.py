import tkinter as tk
root = tk.Tk()

label = tk.Label(root, text = 'Label')
label.grid(column = 3, row = 8)

button = tk.Button(root, text = 'Button')
button.grid(column = 5, row = 1)

root.grid_columnconfigure(4, minsize=100)