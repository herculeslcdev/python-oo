from car import Car

gol = Car('gol', 'Volks', 2016)

print(gol.year)
print(gol.name)
print(gol.make)

########################################

bmw320 = Car('320', 'BMW', 2016)

print(bmw320.make)

########################################

bmw = Car('320', 'BMW', 2016)

bmw.drive()