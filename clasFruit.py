class Fruit:
#initializing fruit class
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour

    def func(self):
        print("Fruit is " + self.name)
#Code test
f1 = Fruit("apple", "red")
f1.func()
#Result
#Fruit is apple