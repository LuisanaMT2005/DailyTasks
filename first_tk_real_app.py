# pylint: disable=missing-module-docstring
import tkinter as tk
from tkinter import ttk


def calculate(*args): # pylint: disable=unused-argument
    """Convert feet to meters"""
    try:
        value = float(feet.get())
        meters.set(round((value / 3.281), 3))
    except ValueError:
        pass

root = tk.Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S), padx=5, pady=5)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(tk.W, tk.E), padx=5, pady=5)

meters = tk.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(tk.W, tk.E), padx=5, pady=5)

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=tk.W, padx=5, pady=5)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=tk.W, padx=5, pady=5)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=tk.W, padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
