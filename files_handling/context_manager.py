"""Using Context Manager (with)"""
# with keyword closes the file as soon as the usage is over

with open("D:\PYTHON\\files_handling\sample_2.txt", "w") as f:
    f.write("Jai Maharana Pratap")

#try f.read() now
with open("D:\PYTHON\\files_handling\sample_2.txt", "r") as f:
    print(f.read())