class House():
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.numbers_of_floors}'

    def __len__(self):
        return self.numbers_of_floors


h1 = House("Котедж", 3)
h2 = House('Дом, милый дом', 10)

print(h1)
print(h2)
print(len(h1))
print(len(h2))