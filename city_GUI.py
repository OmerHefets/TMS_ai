import tkinter as tk

# City size in pixels
CITY_WIDTH = 1200
CITY_HEIGHT = 600
SQUARE_SIZE = 20


class City:

    # City data parameters
    houses = []
    roads = []

    def __init__(self, city_width, city_height, square_size):
        self.city_width = city_width
        self.city_height = city_height
        self.square_size = square_size
        self.create_gui()

    def create_gui(self):
        master = tk.Tk()
        city = tk.Canvas(master, width=self.city_width, height=self.city_height)
        city.pack()

        self.create_empty_city(city)
        tk.mainloop()

    def create_empty_city(self, canvas):
        squares_width = int(self.city_width / self.square_size)
        squares_height = int(self.city_height / self.square_size)
        for i in range(squares_height):
            for j in range(squares_width):
                width_pixel = j * self.square_size
                height_pixel = i * self.square_size
                canvas.create_rectangle(width_pixel, height_pixel,
                                        width_pixel + self.square_size, height_pixel + self.square_size,
                                        fill="lawn green")


my_city = City(CITY_WIDTH, CITY_HEIGHT, SQUARE_SIZE)
