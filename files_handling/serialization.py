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
