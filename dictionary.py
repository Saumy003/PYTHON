# Dictionary in python.
# EX :--1
employeeid = {
    344 : "Harry",
    3   : "Sammy",
    179 : "Holly",
    456 : "Boid"
}
print(employeeid[456])   # output :- Boid

# EX :--2  Accessing single values.

student = {
    "name" : "Lewis",
    "gender" : "Male",
    "DOB" : 2006,
    "Qualification" : "BCA"
}
print(student["DOB"])     #output :- 2006

# EX :-- 3  Accessing all keys.
info = {
    "name" : "Jacob",
    "age"  : 20,
    "eligible" : True
}
print(info.keys())

# EX :--4   Accessing all values.
price = {
    "soap" : 64,
    "oil"  : 99,
    "sunscreen" : 899
}
print(price.values())

# EX :-- 5   Accessing key-value pair.
job = {
    1 : "Doctor",
    2 : "Army",
    3 : "Police"
}
print(job.items())