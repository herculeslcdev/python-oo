class Car:

    x = 'Abcd'

    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year

    def drive(self):
        print(self.name + ' started')
