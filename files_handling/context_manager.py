"""Using Context Manager (with)"""
# with keyword closes the file as soon as the usage is over

with open("D:\\PYTHON\\files_handling\\sample_2.txt", "w") as f:
    f.write("Jai Maharana Pratap")

# #try f.read() now
with open("D:\\PYTHON\\files_handling\\sample_2.txt", "r") as f:
    print(f.read())


# # moving with in the file -> 10 char then 10 char
with open("D:\\PYTHON\\files_handling\\sample_1.txt", "r") as f:
    print(f.read(10))   # print first 10 char
    print(f.read(10))   # print next 10 char

# # benefit ? to load big file in memory
big = ["Radhe Radhe" for i in range(110)]
with open("D:\\PYTHON\\files_handling\\big.txt" , "w") as f:
    f.writelines(big)

# # To open big file in chunks
with open ("D:\\PYTHON\\files_handling\\big.txt", "r") as f:
    chunk_size = 11
    while len(f.read(chunk_size)) > 0:
        print(f.read(chunk_size), end=" ")
        f.read(chunk_size)

# seek and tell method

with open("D:\\PYTHON\\files_handling\\sample_1.txt", "r") as f:
    print(f.read(10))
    print(f.tell())

#seek()
with open("D:\\PYTHON\\files_handling\\sample_1.txt", "r") as f:
    print(f.read(10))
    print(f.tell())
    print(f.seek(5))
    print(f.tell())

# seek during write
with open("D:\\PYTHON\\files_handling\\sample_1.txt", "w") as f:
    f.write("Hello")
    f.seek(0)
    f.write("X")