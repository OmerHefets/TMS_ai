import tkinter as tk
import numpy as np
import Infrastructure as inf

# City size in pixels
CITY_WIDTH = 1200
CITY_HEIGHT = 600
SQUARE_SIZE = 20


class City:

    # City data parameters:
    # Coordinate data
    city_data = []
    # Data about infrastructure
    houses = []
    roads = []

    def __init__(self, city_width, city_height, square_size):
        self.city_width = city_width
        self.city_height = city_height
        self.square_size = square_size
        self.city_data = np.zeros((city_height, city_width))
        self.master = tk.Tk()
        self.create_gui()

    def create_gui(self):
        city = tk.Canvas(self.master, width=self.city_width, height=self.city_height)
        city.pack()

        self.create_empty_city(city)
        tk.mainloop()

    def create_empty_city(self, canvas):
        for i in range(int(self.city_height / self.square_size)):
            for j in range(int(self.city_width / self.square_size)):
                width_pixel = j * self.square_size
                height_pixel = i * self.square_size
                canvas.create_rectangle(width_pixel, height_pixel,
                                        width_pixel + self.square_size, height_pixel + self.square_size,
                                        fill="lawn green")
        b = tk.Button(self.master, text="Hello", command=self.check)
        b.pack(side="left")
        b2 = tk.Button(self.master, text="trial", command=self.create_building)
        b2.pack(side="right")

    def check(self):
        print(self.city_data.shape)

    def create_building(self):
        window = tk.Tk()
        window.title("Add a building")
        l_name = tk.Label(window, text="House Name:")
        l_name.grid(column=0, row=0)
        e_name = tk.Entry(window)
        e_name.grid(column=1, row=0)
        l_ul_x = tk.Label(window, text="Upper Left X:")
        l_ul_x.grid(column=0, row=1)
        e_ul_x = tk.Entry(window)
        e_ul_x.grid(column=1, row=1)
        l_ul_y = tk.Label(window, text="Upper Left Y:")
        l_ul_y.grid(column=0, row=2)
        e_ul_y = tk.Entry(window)
        e_ul_y.grid(column=1, row=2)
        l_br_x = tk.Label(window, text="Bottom Right X:")
        l_br_x.grid(column=0, row=3)
        e_br_x = tk.Entry(window)
        e_br_x.grid(column=1, row=3)
        l_br_y = tk.Label(window, text="Bottom Right Y:")
        l_br_y.grid(column=0, row=4)
        e_br_y = tk.Entry(window)
        e_br_y.grid(column=1, row=4)
        values_arr = [e_ul_x, e_ul_y, e_br_x, e_br_y]
        b_cancel = tk.Button(window, text="Cancel", command=lambda: self.save_data(values_arr=values_arr, house=e_name))
        b_cancel.grid(column=0, row=5)
        # add save function with a Building class creation
        b_save = tk.Button(window, text="Save", command=lambda: self.save_data(values_arr=values_arr, house=e_name))
        b_save.grid(column=1, row=5)

        window.mainloop()

    @staticmethod
    def save_data(infr, values_arr, house):
        if infr == "Building":

        for value in values_arr:
            print(value.get())


my_city = City(CITY_WIDTH, CITY_HEIGHT, SQUARE_SIZE)
