class Account:

    def __init__(self, number):
        self.number = number
        self.__total = 0

    def deposit(self, value):
        self.__total += value

    def withdraw(self, value):
        self.__total -= value

    def get_total(self):
        return self.__total

