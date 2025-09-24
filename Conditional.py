# Some coding examples on Conditional Statement in Python.

#EX :-1

age = int(input("enter the age :"))
if(age>=18):
    print("can vote and apply for license")
else:
    print("can not drive")

#EX :-2

light = "pink"
if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("light is broken")

# EX :- 3

marks = int(input("enter marks:"))
if(marks>=90):
    print("GRADE A")
elif(marks>=80 and marks<90):
    print("GRADE B")
elif(marks>=70 and marks<80):
    print("GRADE C")
else:
    print("GRADE D")


   
