class House:
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __len__(self):
        return self.numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors == other.numbers_of_floors

    def __lt__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors < other.numbers_of_floors

    def __le__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors <= other.numbers_of_floors

    def __gt__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors > other.numbers_of_floors

    def __ge__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors >= other.numbers_of_floors
        else:
            return

    def __ne__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return self.numbers_of_floors != other.numbers_of_floors

    def __add__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return House(self.name, self.numbers_of_floors + other)

    def __iadd__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return House.__add__(self, other)

    def __radd__(self, other):
        if isinstance(other, House) or isinstance(other, int):
            return House.__add__(self, other)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
