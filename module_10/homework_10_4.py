from threading import Thread, Lock
from time import sleep
from queue import Queue

class Table:
    def __init__(self, number):
        self.number = number
        self.is_busy = False

class Customer(Thread):
    def __init__(self, customer_id, table, cafe):
        super().__init__()
        self.customer_id = customer_id
        self.table = table
        self.cafe = cafe

    def run(self):
        print(f'Посетитель номер {self.customer_id} сел за стол {self.table.number}.')
        sleep(5)
        print(f'Посетитель номер {self.customer_id} покушал и ушёл.')
        with self.cafe.lock:
            self.table.is_busy = False
            self.cafe.check_queue()

class Cafe:
    def __init__(self, tables):
        self.queue = Queue()
        self.tables = tables
        self.customer_id = 0
        self.lock = Lock()

    def customer_arrival(self):
        while self.customer_id < 20:
            self.customer_id += 1
            print(f'Посетитель номер {self.customer_id} прибыл.')
            self.serve_customer(self.customer_id)
            sleep(1)


    def serve_customer(self, customer_id):
        with self.lock:
            available_table = None
            for table in self.tables:
                if not table.is_busy:
                    available_table = table
                    break

            if available_table is not None:
                available_table.is_busy = True
                customer = Customer(customer_id, available_table, self)
                customer.start()
            else:
                print(f'Посетитель номер {customer_id} ожидает свободный стол.')
                self.queue.put(customer_id)

    def check_queue(self):
        while not self.queue.empty():
            available_table = None
            for table in self.tables:
                if not table.is_busy:
                    available_table = table
                    break

            if available_table is not None:
                next_customer_id = self.queue.get()
                available_table.is_busy = True
                customer = Customer(next_customer_id, available_table, self)
                customer.start()
            else:
                break


# Создание столиков в кафе
table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]

# Инициализация кафе
cafe = Cafe(tables)

# Запуск потока для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидание завершения работы прибытия посетителей
customer_arrival_thread.join()


