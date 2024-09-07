import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        day = 0

        print(f'{self.name}, на нас напали!')
        while enemy > 0:
            if enemy > 0:
                enemy -= self.power
                time.sleep(1.0)
                day += 1
                if enemy < 0:
                    enemy = 0
            print(f'{self.name} сражается {day} дней(дня).., '
                  f'осталось {enemy} войнов.')
        print(f'{self.name} одержал победу спустя {day} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
