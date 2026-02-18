# sum of two number using function 

def cal_sum(a, b):     #function definition & a and b are parameters
    sum = a + b
    print(sum)
    return sum

cal_sum(5, 10)         #function call
cal_sum(2, 16)
cal_sum(12, 17)

# average of 3 numbers

def cal_avg(a, b, c):
    avg = (a+ b+ c) /3
    print(avg)
    return avg

cal_avg(4, 6, 10)

# product of two number 

def cal_prod(a = 4, b = 2):    # default parameter
    print(a*b)
    return a*b

cal_prod()                     #no arguments passed

# *args
#allows us to pass a variable number of non-keyword arguments to function
def multiply(*args):
    product = 1
    for i in args:
        product = product * i

    return product
        
print(multiply(1,2,3,4,5,6))   #720

#  **kwargs
#  **kwargs allows us to pass any number of keyword arguments.
#  Keywords arguments means that they contain a key-value pair, like a python dictionary.

def display(**kwargs):
    for (key,value) in kwargs.items():
        print (key , "->" , value)

display(india="delhi",srilanka = "colombo" , nepal = "kathmando")

# Nested function
# Example 1
def g(x):
    def h():
        x = "abc"
    x = x +1
    print("in g(x): x=" , x)       # x = 4
    h()
    return x

x = 3 
z = g(x)

# Example 2
def g(x):
    def h(x):
        x = x + 1
        print("in h(x): x =" , x)
    x = x + 1
    print("in g(x): x=" , x)
    h(x)
    return x

x = 3
z = g(x)
print("in main program scope: x =" , x)
print("in main program scope: z =" , z)
