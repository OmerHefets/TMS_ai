"""
Testing the Tkinter GUI for beginners...
"""

import time
import tkinter as tk

master = tk.Tk()
c_width = 1200
c_height = 600

city = tk.Canvas(master, width=c_width, height=c_height)
city.pack()

city.create_rectangle(0, 0, 20, 20, fill="lawn green")
city.create_rectangle(20, 0, 40, 20, fill="red")
time.sleep(1)

tk.mainloop()




