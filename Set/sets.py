# Sets is a datatype that does contains duplicates values.

a = {1,2,3,4,2,3,6,1}
print(a)

info = {"Carla", 19, 5.8, True, 19}
print(info)         #also sets are unordered collection of data items

# Create an empty set.
marks = {}
print(type(marks))  #OUTPUT :- <class'dict'>

marks1 = set()
print(type(marks1))   #OUTPUT :- <class'set'>

# more ex in sets.

student = {"Tim Cook", 56, True, 6.1, True,}
for val in student:
    print(val)