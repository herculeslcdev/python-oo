from car import Car

gol = Car()
# instance atribute
print(gol.x)
# class atribute
print(Car.x)
# doesn't work
# print(Car.year)

gol2 = Car()
# right way
print(gol2.year)