# Dictonary in python

#empty dic
dic ={}
print(dic)      

#dictonary syntax
d = { "name" : "nitish", "gender": "male"}
print(d)


# 2d dictonary
s = {
    "name": "nitish", 
    "college" : "SIT SITAMARHI",
    "sem" : 1,
    "subjects": {
        "dsa" : 62,
        "maths": 67,
        "english": 55
    }
}
print(s)

#using sequence and dict function
d1 = dict([('name', 'jhon'), ('age', 22), (5, 3)])
print(d1)

#duplicate keys
d2 = {'name': 'chiku', 'name': 'saumy'}
print(d2)                              #{'name': 'saumy'}

#mutable items as key
d3 = {"name": "virat", (1, 2, 3): 5}
print(d3)                  # tuple is allowed , but lists are not allowed

#Accessing items
my_dict = {"hobby": "Painting", "color": "green", "age": 21}
print(my_dict["hobby"])
print(my_dict.get("age"))

#adding new key-value pair
d = { "name" : "nitish", "gender": "male"}
d['weight'] = 60
print(d)           #{'name': 'nitish', 'gender': 'male', 'weight': 60}

#remove key-value
my_dict = {"hobby": "Painting", "color": "green", "age": 21}
my_dict.pop("age")
print(my_dict)

#editing key-value pair
