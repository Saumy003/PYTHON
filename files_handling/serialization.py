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