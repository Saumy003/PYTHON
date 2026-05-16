# deserialization

import json

with open("D:\\PYTHON\\files_handling\\demo_1.json", "r") as f:
    # print(json.load(f))

    d = json.load(f)
    print(d)
    print(type(d))


# deserialize in tuple

with open("D:\\PYTHON\\files_handling\\demo_tuple.json", "r") as f:
    print(json.load(f))


# deserialize in nested dict

with open("D:\\PYTHON\\files_handling\\nested_dict.json", "r") as f:
    print(json.load(f))


# deserialization of custom object

# as a string
with open("D:\\PYTHON\\files_handling\\object.json", "r") as f:
    print(json.load(f))
    
# as a dict

with open("D:\\PYTHON\\files_handling\\object_dict.json", "r") as f:
    print(json.load(f))