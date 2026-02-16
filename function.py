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
        
print(multiply(1,2,3,4,5,6))