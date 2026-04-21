# String 

# str1 = "developer "
# str2 = "chiku"

# print(str1 + str2)
# print(str1> str2)
# print(str2 * 3)

# 18

# str3 = "pythonismyfavoraitelanguange"
# count = 0

# for ch in str3:
#     count += 1

# print(count)

#19
# str4 = "listen"
# str5 = "silent"

# str4.lower()
# str5.lower()

# if sorted(str4) == sorted(str5):
#     print("Stings are anagrams")
# else:
#     print("not anagrams")

# 20

# str6 = "abcdefghijklmn"
# str7 = "ijkl"

# if str7 in str6:
#     print("sub-string hai")
# else:
#     print("na bhai nahi h substring")

# 14
# n = 4
# for row in range(1, n+1):
#     for col in range(1, row+1):
#         print("*", end=" ")
#     print()
    
# 15
# num = 8
# for i in range(1, 13):
#     num = 8 * i
#     print(num)

# 10
# num = 7

# def fibo(num):
#     if num==0 or num==1:
#         return num
#     return fibo(num-1) + fibo(num-2)

# fibonnaci = fibo(num)
# print("req fibo num:", fibonnaci)

#16
# choice = input("Enter a character:")

# if len(choice) != 1:
#     print("Please enter only a single character.")
# else:
#     if choice >= "0" and choice <= "9":
#         print("It is a digit.")
#     elif choice >= "a" and choice <= "z":
#         print("It is a lowercase character.")
#     elif choice>= "A" and choice <= "Z":
#         print("It is an uppercase character.")
#     else:
#         print("It is a special character.")

#17
# a = 20.5
# print(round(a))

# 13
# for num in range (1, 21):
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# 21
# str1 = "helloiamchiku"
# for i in range(0, len(str1)):
#     print(str1[i])

# String slicing
# a = "code and debug"
# b = a[::-1]
# print(b)


# my_string = input("Enter your string:")
# if my_string == my_string[::-1]:
#     print("yes")
# else:
#     print("no")

# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You can vote")

# else:
#     print("You can not")

# a = int(input("Enter first number:"))
# b = int(input("Enter second number:"))

# if a > b:
#     print("a is greatest number")
# else:
#     print("b is gratest")

# num = int(input("enter a number:"))
# if num % 2 == 0:
#     print("Given number is even")
# else:
#     print("given number is odd")

# print sum sum of even number from 1 to 50
# count = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         count = i + count
# print(count)

# print sum sum of odd number from 1 to 50
# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         continue
#     else:
#         sum = sum +i

# print(sum)

# print fsctorial of the given number
# 1! == 1 and 0! == 1
# num = int(input("enter the number:"))
# def factorial(num):
#     if num ==1 or num == 0:
#         return 1
#     return  num * factorial(num-1)

# result = factorial(num)
# print(result)

# 17
# n = int(input("enter number of terms: "))

# a = 0
# b = 1
# count = 0

# while count < n:
#     print(a, end=" ")
#     c = a + b
#     a = b
#     b = c
#     count += 1

# 12
# for num in range(20, 51):
#     if num>1:
#         for i in range(2, num):
#             if num % i == 0:
#                 break
#         else:
#             print(num)

# 
        
