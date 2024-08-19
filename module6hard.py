class Figure:
    sides_count = 0

    def __init__(self, __color, __sides):
        filled = False
        self.__sides = __sides
        if len(self.__sides) != self.sides_count:
            self.__sides = [1]*self.sides_count
        self.__color = __color


    def get_color(self):
        color_list = list(self.__color)
        return color_list

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        if r in [i for i in range(0, 256)]:
            if g in [i for i in range(0, 256)]:
                if b in [i for i in range(0, 256)]:
                    self.__color = r, g, b
                    return self.__color

    def set_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        self.__is_valid_color(r, g, b)

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

    def get_sides(self):
        return list(self.__sides)

    def __len__(self):
        perim = 0
        for i in self.__sides:
            perim += i
        return perim


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color=[], *__sides):
        super().__init__(__color, __sides)
        # if len(self.get_sides()) != self.sides_count:
        #     # if isinstance(Figure, Circle):  # and self.cor_sides() is False:
        #     self.__sides = [1]
        __radius = __sides[0] / (2 * 3.14)

    def get_square(self):
        square = 3.14 * (self._Figure__sides[0] ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color=[], *__sides):
        super().__init__(__color, __sides)

        __height = 2 * self.get_square() / __sides[0]

    def get_square(self):
        half_perim = 0.5 * (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2])
        square = (half_perim * (half_perim - self._Figure__sides[0]) *
                  (half_perim - self._Figure__sides[1]) * (half_perim - self._Figure__sides[2])) ** 0.5
        __height = 2 * self.get_square() / self._Figure__sides[0]
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color=[], *__sides):
        super().__init__(__color, __sides)
        cube_sides = __sides
        if len(cube_sides) == 1:
            self._Figure__sides = __sides * self.sides_count
        # if len(self._Figure__sides) == 1:
        #     __sides = [__sides]*self.sides_count
        else:
            self.sides = __sides



    def get_volume(self):
        volume = self._Figure__sides[0] ** 3
        return volume


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
#
# # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
#
# # Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

