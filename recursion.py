# recursive function

# print 5 to 1 backward.

def show(n):
    if(n ==0):
        return
    print(n)
    show(n-1)
show(5)

# factorial of n = 5

def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return n * fact(n - 1)

print(fact(9))

