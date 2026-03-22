# 1 .update()      --> add new items(key-value pairs).
ep1 = {122:45, 456: 89, 340: 29}
ep2 = {222:87, 383:98}
ep1.update(ep2)
print(ep1)

# 2 .clear()    -->  removes all the items.
marks = {1:45, 2:67, 3:98, 4:63, 5:83}
marks.clear()
print(marks)

# 3 .pop()    --> remove item whose key is passed as a parameter.
mrp = {"apple" : 120, "pears" : 100, "orange" : 80}
mrp.pop("apple")
print(mrp)

# 4 .popitem()   --> remove last key-value pair(item).
sports = {1: "golf", 25: "cricket", 3: "football", 7: "baseball"}
sports.popitem()
print(sports)

# 5. get()
my_dict = {
    "name" : "Anirudh",
    "age" : 28,
    "gender" : "Male",
}

print(my_dict.get("name"))    # to get a value

# 6  to update any value of the key
studentid = {
    111 : "Roman",
    222 : "Thomas",
    333 : "Max",
    444 : "Lucifer"
}

# to change the student name at 333 and update new name as"Chris Evans"
studentid[333] = "Chris Evans"
print(studentid)