class Building:

    def __init__(self, x1, y1, x2, y2, house_name):
        self.house_name = house_name
        # upper left:
        self.ul_x = x1
        self.ul_y = y1
        # bottom right:
        self.br_x = x2
        self.br_y = y2
        self.size = self.infr_size_calc(self.ul_x, self.ul_y, self.br_x, self.br_y)

    def infr_size_calc(self, ul_x, ul_y, br_x, br_y):
        x = br_x - ul_x
        y = ul_y - br_y
        size = x * y
        return size


# (x1, y1) = (1, 5) | (x2, y2) = (5, 1)
b = Building(1, 5, 5, 1, "lel")
print(b.size)
