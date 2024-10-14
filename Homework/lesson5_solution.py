"""Классы, ООП"""


# 1. Прямоугольник.
class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self.weight = width

    def area(self):
        return self.height * self.weight

    def perimeter(self):
        return (self.height + self.weight) * 2


rect = Rectangle(2, 4)
a = (rect.area())
p = (rect.perimeter())
print(a)
print(p)


# 2. Автомобиль.

class Car:
    def __init__(self, make, max_speed):
        self.make = make
        self.max_speed = max_speed
        self.speed = 0

    def display_speed(self):
        print(self.speed)

    def accelerate(self):
        if self.speed + 10 <= self.max_speed:
            self.speed += 10
        else:
            self.speed = self.max_speed

    def brake(self):
        if self.speed - 10 > 0:
            self.speed -= 10
        else:
            self.speed = 0

    #  Варианты с функцией min, max:
    # def accelerate(self):
    #     self.speed = min(self.max_speed, self.speed + 10)
    #
    # def brake(self):
    #     self.speed = max(0, self.speed - 10)


my_toyota = Car("Toyota", 180)

my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.accelerate()
my_toyota.display_speed()


# 3. Интернет - банк.

class BankAccount:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if self._balance - amount < 0:
            print("Недостаточно средств")
        else:
            self._balance -= amount

    def get_balance(self):
        return self._balance


account = BankAccount("Maria", 1000)
account.deposit(700)
account.withdraw(90000)
print(account.get_balance())

# 4. Овердрафт.


class OverdraftAccount(BankAccount):
    def withdraw(self, amount):
        self._balance -= amount


jack_account = OverdraftAccount("Jack", 0)
jack_account.withdraw(100)
print(jack_account.get_balance())


        
