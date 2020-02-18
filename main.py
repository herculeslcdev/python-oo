from bank import Account

wesley = Account(123)

# wesley.__total doesn't exists

print(wesley.get_total())
wesley.deposit(1000)
print(wesley.get_total())


