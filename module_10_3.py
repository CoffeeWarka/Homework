import time, random
from threading import Thread, Lock


class Bank:
    def __init__(self):
        self.lock = Lock()
        self.balance = 0


    def deposit(self):
        for i in range(100):
            rand_dep = random.randint(50, 500)
            self.lock.acquire()
            self.balance += rand_dep
            print(f"Пополнение: {rand_dep}. Баланс: {self.balance}")
            time.sleep(0.001)
            self.lock.release()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()


    def take(self):
        for i in range(100):
            rand_take = random.randint(50, 500)
            print(f'Запрос на {rand_take}')
            self.lock.acquire()
            if rand_take <= self.balance:
                self.balance -= rand_take
                print(f"Снятие: {rand_take}. Баланс: {self.balance}")
            else:
                print(f"Запрос отклонён, недостаточно средств")

            self.lock.release()


bk = Bank()

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
