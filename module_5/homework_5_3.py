class Building():
    def __init__(self, numbers_of_floors, building_type):
        self.numbers_of_floors = int(numbers_of_floors)
        self.building_type = str(building_type)

    def __str__(self):
        return f'{self.building_type} {self.numbers_of_floors}'

    def __eq__(self, other):
        return (self.numbers_of_floors == other.numbers_of_floors or
                self.building_type == other.building_type)

b1 = Building(10, 'house')
b2 = Building(2, 'garage')

print(b1)
print(b2)
print(b1 == b2)
