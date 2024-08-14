class Figure:
    valid_color = False
    sides_count = 0
    def __init__(self, __sides=[], __color=[], filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_collor(self):
        color_list = self.__color
        return color_list

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if r in [i for i in range(0,256)]:
            if g in [i for i in range(0,256)]:
                if b in [i for i in range(0,256)]:
                    Figure.valid_color = True
                    return Figure.valid_color

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        if Figure.valid_color:
            self.__color = [self.r, self.g, self.b]





fig = Figure()
fig.set_color(66, 33, 55)
print(fig.get_collor())