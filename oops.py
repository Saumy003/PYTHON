# Basic Class & Object 
# problem :--> Create a Student class with attributes like name & age. Then create an instance of this class.

# 1st Approch
class Student:
     name = "karan"
     age = 19
s1 = Student()
print(s1.name)
print(s1.age)

# 2nd Approah
class Car:
    def __init__(self, brand, model):     #constructor
        self.brand = brand
        self.model = model

my_car = Car("Toyota", "Corolla")
print(my_car.brand)
print(my_car.model)

# methods in oop

class Boy:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def hello(self):                      #Method in oop
        print("welcome boy", self.name)
             
s2 = Boy("Dewald Brevis", 25)
s2.hello()

# static methods 
class University:
    def __init__(self, name):
        self.name = name
    
    @staticmethod              # decorater --> convert function to be a static function.
    def college():             # doesn't use self parameter.
        print("SIT Sitamarhi")

s3 = University("BEU Patna")
s3.college()
