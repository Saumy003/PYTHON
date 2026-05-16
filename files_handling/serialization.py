# serialization using json module
# list

import json

L = [1, 2, 3, 4, 5]

with open("D:\\PYTHON\\files_handling\\demo.json", "w") as f:
    json.dump(L, f)

# dictonary

d ={
    "name" : "Dario",
    "age" : 49,
    "gender" : "male"
}

with open("D:\\PYTHON\\files_handling\\demo_1.json", "w") as f:
    json.dump(d, f, indent=4)


# serialize in tuple --> {iss me thoda alag hai}

t = (1, 2, 3, 4, 5)

with open("D:\\PYTHON\\files_handling\\demo_tuple.json", "w") as f:
    json.dump(t, f)


# serialize in nested dict

dic = {
    "name" : "Altman",
    "marks" : [79 ,88, 94, 97, 84]
}

with open("D:\\PYTHON\\files_handling\\nested_dict.json", "w") as f:
    json.dump(dic, f)

# serialization of custom object

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# format to printed in is: name -> Nitish Singh age-> 33 gender -> male


person = Person("Nitish", 33, "male")

#as a string

def show_object(person):
    if isinstance(person, Person):
        return "name ->{}  age-> {} gender -> {}".format(person.name, person.age, person.gender)

with open("D:\\PYTHON\\files_handling\\object.json", "w") as f:
    json.dump(person, f, default=show_object)

# as a dict
def show_dict(person):
    if isinstance(person, Person):
        return {"name" : person.name ,"age" : person.age, "gender" : "male" }

with open("D:\\PYTHON\\files_handling\\object_dict.json", "w") as f:
    json.dump(person, f, default=show_dict, indent=4)