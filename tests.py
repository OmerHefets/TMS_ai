"""
Testing the Tkinter GUI for beginners...
"""

import time
import tkinter as tk


def save_data():
    print(E1.get())
    city.create_rectangle(0, 0, 40, 20, fill="red")


master = tk.Tk()
c_width = 1200
c_height = 600

city = tk.Canvas(master, width=c_width, height=c_height)
city.pack()

city.create_rectangle(0, 0, 20, 20, fill="lawn green")

L1 = tk.Label(city, text="User Name")
L1.pack(side="left")
E1 = tk.Entry(city, bd=5)
E1.pack(side="right")
E1.focus_set()
b = tk.Button(city, text="Save", command=save_data)
b.pack(side="bottom")

tk.mainloop()



"""
city_data = [[0 for x in range(20)] for y in range(50)]
print(city_data)
"""
