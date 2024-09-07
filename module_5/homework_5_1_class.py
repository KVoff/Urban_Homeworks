from colorama import Fore  # раскраска текста
class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(Fore.RED + 'There is no such floor')
        else:
            for i in range(0, new_floor):
                i = i + 1
                print(Fore.GREEN + str(i))