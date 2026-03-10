# inheitance concepts in python

class Animal:                              # Animal is the parent class

    def __init__(self, name:str , age:int):
        self.name = name
        self.age = age

    def eat(self):
        print("I am eating")
    def sleep(self):
        print("I am sleeping")

    def move():
        print("I am moving")

class Dog(Animal):            # Dog-> child class              #Inheritance
    
    def __init__(self , name , age , bread):
        super().__init__(name , age)
        self.bread = bread
    
    def bark(self):
        print("I am barking")

    def move(self):
        print(f"{self.name} moves with 4 legs")            #Polymorphism -> Over-ride

    def display(self):
        print(f"Name is {self.name} and age is {self.age}")

dog = Dog("Tommy", 5 , "Siberian Husky")
dog.display()
dog.move()
