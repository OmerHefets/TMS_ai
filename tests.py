"""
Testing the Tkinter GUI for beginners...
"""

import tkinter as tk

master = tk.Tk()
c_width = 1000
c_height = 1000

city = tk.Canvas(master, width=c_width, height=c_height)
city.pack()

city.create_rectangle(0, 0, 20, 20, fill="yellow")
city.create_rectangle(20, 0, 40, 20, fill="red")

tk.mainloop()






