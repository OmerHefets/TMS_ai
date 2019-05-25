"""
Testing the Tkinter GUI for beginners...
"""

import time
import tkinter as tk


def save_data():
    print(E1.get())


master = tk.Tk()
c_width = 1200
c_height = 600

city = tk.Canvas(master, width=c_width, height=c_height)
city.pack()

city.create_rectangle(0, 0, 20, 20, fill="lawn green")
city.create_rectangle(20, 0, 40, 20, fill="red")


tk.mainloop()

window = tk.Tk()
L1 = tk.Label(window, text="User Name")
L1.pack(side="left")
E1 = tk.Entry(window, bd=5)
E1.pack(side="right")
E1.focus_set()
b = tk.Button(window, text="Save", command=save_data)
b.pack(side="bottom")
window.mainloop()

"""
city_data = [[0 for x in range(20)] for y in range(50)]
print(city_data)
"""
