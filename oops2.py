# 4 pillars of OOPS

# 1. Abstraction  --> hiding unneccessary details of a class
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start():
        self.clutch = True
        self.acc = True
print("car started..")

# 2. Encapsulation --> wrapping of data and function in single unit(object).
class Boy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):                      # Method in oop are eg of encapsulation.
        print("welcome boy", self.name)
             
s2 = Boy("Dewald Brevis", 25)
s2.hello()

# 3. Inheritance --> when one class derives the properties & methods of another class.
class Bike:
    @staticmethod
    def start():
        print("bike started..")

    @staticmethod
    def stop():
        print("bike stopped.")

class Bullet(Bike):              #  single inheritance.
    def __init__(self, name):
        self.name = name

bike1 = Bullet("Guerrilla")
print(bike1.start())

# 4. Polymorphism  --> Same operators is allowes to have different meaning acc. to context.

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img

    def showNumber(self):
        print(self.real, "+", self.img, "i")

    def __add__(self, num2):                  # dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)

num1 = Complex(1, 3)
num1.showNumber()

num2 = Complex(4, 6)
num2.showNumber()

num3 = num1 + num2
num3.showNumber()


