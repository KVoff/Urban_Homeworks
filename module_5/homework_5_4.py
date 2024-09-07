class Buildings():
    total = 0

    def __init__(self):
        return
    def count_of_buildings(self):
        while self.total < 40:
            Buildings.total += 1
            print(Buildings.total)
        else:
            print('Construction completed')

b1 = Buildings()
b1.count_of_buildings()





