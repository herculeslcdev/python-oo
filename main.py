from bank import Bank1Account
from bank import Bank2Account

wesley = Bank1Account(12)

print(wesley.__class__)
print(type(wesley))

##################################

b1 = Bank1Account(123)
b2 = Bank2Account(123, 'xpto')

print(b2.cvv)





