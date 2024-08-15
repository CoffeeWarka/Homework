class Figure:
    sides_count = 0

    def __init__(self, __color=[], __sides=[], filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_collor(self):
        color_list = list(self.__color)
        return color_list

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        if r in [i for i in range(0,256)]:
            if g in [i for i in range(0,256)]:
                if b in [i for i in range(0,256)]:
                    self.__color = r, g, b
                    return self.__color

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.__is_valid_color(r,g,b)





fig = Figure((200,200,200), 10)
fig.set_color(44, 33, 55)
print(fig.get_collor())
