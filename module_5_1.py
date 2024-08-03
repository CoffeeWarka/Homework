class House():
    def __init__(self, name, numbers_of_floors):
        self.name = name
        self.numbers_of_floors = numbers_of_floors


    def go_to(self, new_floor):
        floor = 1
        if new_floor > self.numbers_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            while floor <= new_floor:
                print(floor)
                floor +=1



h1 = House("Котедж", 3)
h2 = House('Дом, милый дом', 10)
h1.go_to(2)
h2.go_to(112)