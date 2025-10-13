# Break & Continue
i = 1
while i <= 5 :
    print(i)
    if(i == 3) :
        break
    i += 1

x = 0
while x <= 5 :
    if(x == 3) :
        x += 1
        continue  #skip
    print(x)
    x += 1

# For loop 
# ex 1.

nums = [1, 2, 3, 4, 5]
for val in nums :
    print(val)
# ex 2.

fruits = ["apple", "banana", "grapes", "mango"]
for val in fruits :
    print(val)

# ex 3.

name = "Jack"
for char in name :
    print(char)
else :
    print("END")



