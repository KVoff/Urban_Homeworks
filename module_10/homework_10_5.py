import multiprocessing
import time

class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()
        self.lock = multiprocessing.Lock()

    def process_request(self, request):
        product, action, amount = request
        if action == 'receipt':
            if product in self.data:
                self.data[product] += amount
            else:
                self.data[product] = amount
        elif action == 'shipment':
            if product in self.data and self.data[product] > 0:
                self.data[product] -= amount
                if self.data[product] < 0:
                    self.data[product] = 0

    def run(self, requests):
        processes = []
        for request in requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()
            time.sleep(0.01)

            for p in processes:
                p.join()

if __name__ == "__main__":
    # Создаем менеджера склада
    manager = WarehouseManager()

    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50)
    ]

    # Запускаем обработку запросов
    manager.run(requests)

    # Выводим обновленные данные о складских запасах
    print(dict(manager.data))

