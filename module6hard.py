class Figure:
    sides_count = 0

    def __init__(self, __color=[], __sides=[], filled=False):
        # if isinstance(Figure, Circle) and self.cor_sides() is False:
        #     self.__sides = [1]
        # elif isinstance(Figure, Triangle) and self.cor_sides() is False:
        #     self.__sides = [1, 1, 1]
        # elif isinstance(Figure, Cube) and self.cor_sides() is False:
        #     self.__sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        # else:
        # if len([__sides]) == self.sides_count:
        #     self.__sides = __sides
        # else:
        #     if isinstance(Figure, Circle): #and self.cor_sides() is False:
        #         __sides = [1]
        #     elif isinstance(Figure, Triangle): #and self.cor_sides() is False:
        #         __sides = [1, 1, 1]
        #     elif isinstance(Figure, Cube): #and self.cor_sides() is False:
        #         __sides = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.__sides = __sides
        self.__color = __color
        self.filled = filled

    def cor_sides(self):
        sides_list = [self.__sides]
        if len(sides_list) == self.sides_count:
            return True
        else:
            return False

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
                self.__sides = list(self.new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        perim = 0
        for i in self.__sides:
            perim += i
        return perim


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color=[], __sides=[], filled=False):
        super().__init__(__color, __sides, filled)
        if len([self._Figure__sides]) != self.sides_count:
            self.__sides = 1
        else:
            self.__sides = __sides
        __radius = self.__sides / (2 * 3.14)

    def get_square(self):
        square = 3.14 * (len(self.__sides) ** 2)
        return square


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color=[], __sides=[], filled=False):
        super().__init__(__color, __sides, filled)

        __height = 2 * self.get_square() / __sides[0]

    def get_square(self):
        half_perim = 0.5 * (self._Figure__sides[0] + self._Figure__sides[1] + self._Figure__sides[2])
        square = (half_perim * (half_perim - self._Figure__sides[0]) *
                  (half_perim - self._Figure__sides[1]) * (half_perim - self._Figure__sides[2])) ** 0.5
        __height = 2 * self.get_square() / self._Figure__sides[0]
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color=[], __sides=[], filled=False):
        super().__init__(__color, __sides, filled)
        self._Figure__sides = [__sides] * self.sides_count

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
