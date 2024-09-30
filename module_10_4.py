from threading import Thread
from time import sleep
from random import randint
import queue
from itertools import cycle
class Table:
    def __init__(self, number, guest = None):
        self.number = number
        self.guest = guest

class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        eat_time = randint(3,10)
        sleep(eat_time)

class Cafe:
    def __init__(self, *tables):
        self.queue = queue.Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        i = 0
        for guest in guests[i:]:
            if i < 5:
                for table in tables[i:]:
                    table.guest = guest
                    table.guest.start()
                    print(f'{guest.name} сел(-а) за стол номер {table.number}')
                    i +=1
                    break
            else:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')







    def discuss_guests(self):
        for table in cycle(tables):
            while table.guest is not None and not table.guest.is_alive():



                print(f'{table.guest.name} покушал(-а) и ушёл(ушла)')
                print(f'Стол номер {table.number} свободен')
                table.guest = None
            # elif self.queue.empty() and table.guest is None:
            #     break




                if not self.queue.empty() and table.guest is None:

                        table.guest = self.queue.get()
                        print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                        table.guest.start()
            # if self.queue.empty() and table.guest is None:
            #     break

            # if self.queue.empty() and not table.guest is None:
            #     break












#Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
