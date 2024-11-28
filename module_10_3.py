import threading
import time
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        counter = 0
        for i in range(100):
            counter += 1
            amount = random.randint(50, 500)
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')

            """Проверяем условие: баланс больше или равен 500 (если не то пополняем до 500)
             и заблокирован замок lock"""

            if self.balance < 500:
                # print(f'Цикл пополнения № {counter} завершен!')
                continue
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            # print(f'Цикл пополнения № {counter} завершен!')
            time.sleep(0.001)

    def take(self):
        counter = 0
        for i in range(100):
            counter += 1
            amount = random.randint(50, 500)
            print(f'Запрос на {amount }')

            """Поверяем условие: 
            - если случайное число меньше баланса - производим списание, иначе проверяем;
            - если поток  deposit 'мертв' а цикл списания еще не завершился - пытаемся списать хоть что-нибудь;
            - иначе открываем замок и пополняем баланс."""

            if amount <= self.balance:
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
            else:
                if not th1.is_alive() and counter < 100:
                    print('Запрос отклонен, недостаточно средств.')
                    # print(f'Цикл снятия № {counter} завершен!')
                    continue
                else:
                    print('Запрос отклонен, недостаточно средств.')
                    self.lock.acquire()

            # print(f'Цикл снятия № {counter} завершен!')
            time.sleep(0.001)


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
