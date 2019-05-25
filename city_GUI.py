import tkinter as tk
import numpy as np

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
        b.pack()

    def check(self):
        print(self.city_data.shape)


my_city = City(CITY_WIDTH, CITY_HEIGHT, SQUARE_SIZE)
