class Figure:
    sides_count = 2

    def __init__(self, __color=[], __sides=[], filled=False):
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def get_color(self):
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

    def __is_valid_sides(self, *args):
        self.args = args
        for i in args:
            if i >= 0 and len(args) == self.sides_count:
                return True
            else:
                return False

    def set_sides(self, *new_sides):
        self.new_sides = new_sides
        if self.__is_valid_sides(*new_sides):
            if len(new_sides) == self.sides_count:
                self.__sides = self.new_sides
            else:
                self.__sides = self.__sides

    def get_sides(self):
        sides = list(self.__sides)
        return sides






fig = Figure((200,200,200), (20,20))
# fig.set_color(44, 33, 55)
# print(fig.get_color())
# fig.set_sides(5,3,12,4,5)
# print(fig.get_sides())
# print(fig.is_valid_sides(11))
fig.set_sides(12,11)
print(fig.get_sides())

# создание массива с одинаковыми значениями в питоне
# import numpy as np
# np.full(
#   shape=10,
#   fill_value=3,
#   dtype=np.int
# )
# > array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3])
