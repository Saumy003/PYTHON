# Functions are continued from here ...
# FUNCTION are 1st class citizens in python --> (python acts as datatypes in python)

# 1. type and id
def square(num):
    return num**2

print(type(square))
print(id(square))

# 2. reassign
x = square
print(id(square))
print(x(3))

# 3.deleting a function
       # del square --> function deleated

# 4.sorting
L = [1,2,3,4,5,square]
print(L[-1](3))           #9

# returing a function
def f():
    def x(a , b):
        return a+b
    return x            # x is function itself

val = f()(3,4)
print(val)              # val = 7

# function as arguments
def func_a():
    print("inside func_a")
def func_b(z):
    print("inside func_b")
    return z()
print(func_b(func_a))

# Lambda function -> samll function
a = lambda x:x**2
print(a(2))        #4

b = lambda x,y: x+y
print(b(3 , 4))    #7

num = lambda x: "even" if x%2 == 0 else "odd"
print(num(8))         # even

# higher order function



