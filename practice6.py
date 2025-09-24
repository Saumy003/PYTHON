# Q 7. WAP to check if a number is entered by the user is odd or even.

num = int(input("enter number:"))
rem = num % 2
if(rem ==0):
    print("EVEN")
else:
    print("ODD")

# Q 8. WAP to find the greatest of three number entered by the user.

a = int(input("enter first number:"))
b = int(input("enter second number:"))
c = int(input("enter third number:"))

if(a>=b and b>=c):
    print("A is greatest")
elif(b>=c):
    print("B is greatest")
else:
    print("C is greatest")

# Q 9. WAP to check if a number is a multiple of 7 or not.

x = int(input("enter any number:"))

if(x % 7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")