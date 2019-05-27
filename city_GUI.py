import tkinter as tk
import numpy as np
import Infrastructure as inf
import helper_functions as hlp

# City size in pixels
CITY_WIDTH = 1200
CITY_HEIGHT = 600
SQUARE_SIZE = 20
# Conventions for grid data
EMPTY = 0
HOUSE = 1
ROAD = 2
TRAFFIC_LIGHT = 3

class City:

    # City data parameters:
    # Coordinate data
    city_data = []
    # Data about infrastructure
    buildings_objects = []
    roads_objects = []
    tr_light_objects = []

    def __init__(self, city_width, city_height, square_size):
        self.city_width = city_width
        self.city_height = city_height
        self.square_size = square_size
        # init city to empty
        self.city_data = np.zeros((city_height, city_width))
        self.master = tk.Tk()
        self.create_gui()

    def create_gui(self):
        city = tk.Canvas(self.master, width=self.city_width, height=self.city_height)
        city.pack()

        self.init_empty_city(city)
        tk.mainloop()

    def init_empty_city(self, canvas):
        for i in range(int(self.city_height / self.square_size)):
            for j in range(int(self.city_width / self.square_size)):
                width_pixel = j * self.square_size
                height_pixel = i * self.square_size
                canvas.create_rectangle(width_pixel, height_pixel,
                                        width_pixel + self.square_size, height_pixel + self.square_size,
                                        fill="lawn green")
        b = tk.Button(self.master, text="Info", command=self.check)
        b.pack(side="left")
        b2 = tk.Button(self.master, text="Edit", command=self.add_building)
        b2.pack(side="right")

    def check(self):
        print(self.city_data.shape)

    def add_building(self):
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
        values_arr = [e_name, e_ul_x, e_ul_y, e_br_x, e_br_y]
        b_cancel = tk.Button(window, text="Cancel", command=lambda: window.destroy())
        b_cancel.grid(column=0, row=5)
        # add save function with a Building class creation
        b_save = tk.Button(window, text="Save", command=lambda: self.create_building(values_arr=values_arr, gui=window))
        b_save.grid(column=1, row=5)

        window.mainloop()

    @staticmethod
    def create_building(values_arr, gui):
        name = values_arr[0].get()
        ul_x = values_arr[1].get()
        ul_y = values_arr[2].get()
        br_x = values_arr[3].get()
        br_y = values_arr[4].get()
        # checking coordinates data types:
        coordinates = [ul_x, ul_y, br_x, br_y]
        for coord in coordinates:
            if not hlp.is_int(coord):
                print("Error, one of the values is not an integer. Try again.")
                gui.destroy()
        # checking for duplications:
        # 


my_city = City(CITY_WIDTH, CITY_HEIGHT, SQUARE_SIZE)
