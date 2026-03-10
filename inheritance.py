# inheitance concepts in python

class Animal:
    def eat(self):
        print("I am eating")
    def sleep(self):
        print("I am sleeping")

class Dog(Animal):
    def bark(self):
        print("I am barking")

dog = Dog()
dog.bark()
dog.eat()
dog.sleep()
