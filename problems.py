# 1. Program to add two numbers.
num1 = 30 
num2 = 40
print("the sum of given two are =" ,num1 + num2)

### another method

num3 = float(input("enter the first number="))
num4 = float(input("enter the second number="))

sum = num3 + num4

print("the sum of both the number are=" , sum)


## code to print prime number
num = int(input("enter the number:"))

for i in range(2,num):
    if(num % i == 0):
        print("not prime")
    else:
        print("it is prime")