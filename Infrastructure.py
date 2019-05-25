class Building:

    def __init__(self, x1, y1, x2, y2, house_name):
        self.house_name = house_name
        # upper left:
        self.x_ul = x1
        self.y_ul = y1
        # bottom right:
        self.x_br = x2
        self.y_br = y2

