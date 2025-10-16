# File input/output in python.
f0 = open("demo.txt", "r")               # reading to a file.
data = f0.read()
print(data)
print(type(data))
f0.close()

# Reading first line of the file.

f1 = open("demo.txt", "r")
line1 = f1.readline()
print(line1)

# Writing to a file.
f2 = open("sample.txt", "w")                # overwrite entire file.
f2.write("Hello\n I am learning Python.")   
f2.close()

f3 = open("sample.txt", "a")                # adds to the file.
f3.write("I will learn DSA soon. ")
f3.close()

# with syntax
with open("demo.txt", "r") as f:
    data = f.read()
print(data)                         # f.close() is not required here.


