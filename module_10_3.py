import threading
import time
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        for i in range(100):
            replenishment = random.randint(50, 500)
            self.balance += replenishment
            print(f'Пополнение: {replenishment}. Баланс: {self.balance}')

            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                continue

            time.sleep(0.001)

    def take(self):
        self.lock.acquire()
        for i in range(100):
            withdrawal = random.randint(50, 500)
            print(f'Запрос на {withdrawal}')

            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств.')
                self.lock.acquire()

        time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
