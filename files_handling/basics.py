# case1 => if the file is not present

f = open("sample_1.txt", "w")
f.write("Hello ! I am learning File Handling")
f.close()

# case2 => if the file is already present

file_2 = open("D:\PYTHON\FILE HANDLING\sample_2.txt", "w")
file_2.write("Jai Rajputana")
file_2.close()

# problem with w mode => it replace previous content in file
# introducing append mode
file = open("D:\PYTHON\\files_handling\sample_2.txt" , "a")
file.write("\nJai Maa Bhawati")
file.close()


# write lines
L = ["hii\n", "hello\n", "kaise ho\n", "main badhiya tum bataoo\n"]
f = open("D:\PYTHON\\files_handling\sample_1.txt", "w")
f.writelines(L)
f.close()

# reading from file 
# using read()
f = open("D:\PYTHON\\files_handling\sample_2.txt", "r")
read_data = f.read()
print(read_data)
f.close

# readline() --> to read line by line
f = open("D:\PYTHON\\files_handling\sample_1.txt", "r")
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

# read entire using readline  {nice concept}

f = open("D:\PYTHON\\files_handling\sample_2.txt", "r")
while True:
    data = f.readline()

    if data == "":
        break
    else:
        print(data, end="")
f.close()
