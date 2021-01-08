#new class

class Food():
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.amount = 15

    def __str__(self):
        return "{},{}".format(self.name, self.color)

    def eat(self):
        self.amount -= 1
        print(self.amount)

    def shop(self):
        self.amout = 15
        print('bought more food')

food1 = Food('apple', 'red')

food1.eat()
food1.eat()
food1.shop()

