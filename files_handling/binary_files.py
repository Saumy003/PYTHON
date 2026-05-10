"""working with binary files"""

# code to create copy of binary files
with open("D:\\PYTHON\\files_handling\\image.avif", "rb") as f:
    with open("D:\\PYTHON\\files_handling\\photo.avif", "wb") as wf:
        wf.write(f.read())

# working with other datatypes
with open("D:\\PYTHON\\files_handling\\sample_1.txt", "w") as f:
    f.write("5")
