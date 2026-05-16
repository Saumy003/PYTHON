"""working with binary files"""

# code to create copy of binary files
with open("D:\\PYTHON\\files_handling\\image.avif", "rb") as f:
    with open("D:\\PYTHON\\files_handling\\photo.avif", "wb") as wf:
        wf.write(f.read())

# working with other datatypes
with open("D:\\PYTHON\\files_handling\\sample_1.txt", "w") as f:
    f.write("5")

with open("D:\\PYTHON\\files_handling\\sample_1.txt", "r") as f:
    print(int(f.read()) + 5)


#working wuth more complex datatypes. ex - Dictonaries

d ={
    "name" : "Dario",
    "age" : 49,
    "gender" : "male"
}

with open("D:\\PYTHON\\files_handling\\sample_1.txt", "w") as f:
    f.write(str(d))


# What is the drawback ?
# ans:- write() argument must be string, not dictonary.

# Due to this drawback of simple file handling serialization and deserialization come in picture.
