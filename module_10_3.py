import time, threading, random


class Bank:
    def __init__(self, balance = 0):
        self.lock = threading.Lock()
        self.balance = balance


    def deposit(self):
        count = 0
        while count < 100:
            rand_dep = random.randint(50, 500)
            self.balance = self.balance + rand_dep
            print(f'Пополнение: {rand_dep}. Баланс: {self.balance}')
            time.sleep(0.001)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            count += 1

    def take(self):
        count = 0
        while count < 100:
            rand_take = random.randint(50, 500)
            print(f'Запрос на {rand_take}')
            if rand_take <= self.balance:
                self.balance = self.balance - rand_take
                print(f'Снятие: {rand_take}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            count += 1

bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')