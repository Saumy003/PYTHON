# Pass by reference:-

class Person:
    def __init__(self , name , gender):
        self.name = name
        self.gender = gender

            # outside the class -> function

def greet(Person):                   # Person class is used as parameter in greet function
    print(f"Hii my is {Person.name} and I am a {Person.gender}.")

p = Person("Akshay" , "Male")
greet(p)

#Encapsulation

