# Q 1. WAF to print the length of a list.
cities = ["delhi" , "gurgaon" , "pune" , "mumbai"]
def print_len(list):
    print(len(list))

print_len(cities)

# Q 2. WAF to print the element of a list in a single line.
heroes = ["thor" , "spiderman" , "ironman" , "hulk" , "superman"]
def print_list(list):
    for item in list:
        print(item, end =" ")
print_list(heroes)

# Q 3. WAF to find the factorial of n.
def cal_fact(n):
    fact = 1
    for i in range(1 , n+1):
        fact *= i
    print(fact)
cal_fact(6)

# Q 4. WAF to covert USD to INR.

def converter(usd_val):
    inr_val = usd_val * 84.25
    print(usd_val, "USD =", inr_val, "INR")
    return inr_val
    
converter(100)