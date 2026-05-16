class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print("Hi my name is", self.name, "and I am", self.age, "years old")

person = Person("Nitish", 33)

# pickle dump

import pickle

with open("D:\\PYTHON\\files_handling\\demo.pkl", "wb") as f:
    pickle.dump(person, f)

# pickle load

with open("D:\\PYTHON\\files_handling\\demo.pkl", "rb") as f:
    p = pickle.load(f)

    p. display_info()