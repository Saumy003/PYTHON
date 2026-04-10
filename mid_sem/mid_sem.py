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

choice = input("Enter a character:")

if len(choice) != 1:
    print("Please enter only a single character.")
else:
    if choice >= "0" and choice <= "9":
        print("It is a digit.")
    elif choice >= "a" and choice <= "z":
        print("It is a lowercase character.")
    elif choice>= "A" and choice <= "Z":
        print("It is an uppercase character.")
    else:
        print("It is a special character.")
    
    


