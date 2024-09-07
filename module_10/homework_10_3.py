from threading import Thread, Lock
import time


class BankAccount:
    def __init__(self):
        self.balance = 1000
        self.lock = Lock()

    def deposit(self, amount):
        with self.lock:
            self.balance += amount
            #time.sleep(1)
            print(f'Deposited {amount}, new balance is {self.balance}')

    def withdraw(self, amount):
        with self.lock:
            self.balance -= amount
            #time.sleep(1)
            print(f'Withdrew {amount}, new balance is {self.balance}')


def deposit_task(account, amount):
    for _ in range(5):
        account.deposit(amount)


def withdraw_task(account, amount):
    for _ in range(5):
        account.withdraw(amount)


account = BankAccount()

deposit_thread = Thread(target=deposit_task, args=(account, 100))
withdraw_thread = Thread(target=withdraw_task, args=(account, 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()

print(f'Final balance is {account.balance}')
