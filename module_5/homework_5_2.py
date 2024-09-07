class House():
    def __init__(self, number_of_floors):
        self.number_of_floors = number_of_floors
        print(f'Количество этажей в начале строительства: {self.number_of_floors}')

    def set_new_number_of_floors(self, floors):
        self.number_of_floors = floors
        print(f'Количество этажей при завершении строительста: {self.number_of_floors}')

house_1 = House(0)
house_1.set_new_number_of_floors(12)