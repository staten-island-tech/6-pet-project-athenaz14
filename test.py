""" """ 
class Calculator():
    def add(x, y):
        print(x + y)
        return x + y

    def add_many(numbers):
        print(sum(numbers))
        return sum(numbers)

    def subtract(numbers):
        return numbers

Calculator.add(5, 6)

class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
""" Bob = Hero("Bob", 200, ["Potion"])
Bob.buy({"title": "Staff", "atk": 30})
print(Bob.__dict__)"""

""" class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")
Bob = BankAccount("Bob", 200)
Bob.deposit(1000)
print(Bob.__dict__)
 """"""
class Pet:
    def __init__(self, name, happiness):
        self.name = name
        self.happiness = happiness
Miso = Pet({"Miso",})
print(Miso.__dict__)

class Interaction:
    def __init__(self, pet, happy_balance):
        self.pet = pet
        self.__happy_balance = happy_balance
    def play(self, total):
        self.__happy_balance += total
    def show_status(self):
        print(f"{self.pet} has {self.__happy_balance}")
Miso = Interaction({"Miso",70})
 """
class Interaction:
    def __init__(self, pet, happy_balance):
        self.pet = pet
        self.__happy_balance = happy_balance

    def play(self, amount):
        self.__happy_balance += amount

    def show_balance(self):
        print(f"{self.pet} has {self.__happy_balance}")

Miso = Interaction("Miso", 1)
Play = input("Do you want to play with the pet?(y/n)")
while Play == "y":
    Miso.play(5)
    print("Miso's happiness has increased!")
    print(Miso.__dict__)
    continue_play = input("Do you want to continue play with the pet?(y/n)")
    if continue_play == "n":
        break
print(Miso.__dict__)
