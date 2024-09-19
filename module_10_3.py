import time, random
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0


    def deposit(self):
        for i in range(100):
            rand_dep = random.randint(50, 500)
            self.balance = self.balance + rand_dep
            print(f'Пополнение: {rand_dep}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            rand_take = random.randint(50, 500)
            print(f'Запрос на {rand_take}')
            if rand_take <= self.balance:
                self.balance = self.balance - rand_take
                print(f'Снятие: {rand_take}. Баланс: {self.balance}')
            elif rand_take > self.balance:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')