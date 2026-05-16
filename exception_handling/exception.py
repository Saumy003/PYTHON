# How to handle Exceptions --> try except block

try:
    with open("sample6.txt", "r") as f:
        print(f.read())

except:
    print("sorry file not found")


# catching specific exception

try:
    m = 5
    f = open("sample9.txt", "r")
    print(f.read())
    print(m)
    print(5/0)
    L = [1, 2, 3]
    L[100]

except FileNotFoundError:
    print("File not Found")
except NameError:
    print("Variable not found")
except ZeroDivisionError:
    print("Can not divide by 0")
except Exception as e:
    print(e)


# try - except - else - finally
try:
    f = open("sample9.txt", "r")

except FileNotFoundError:
    print("file nahi mili")
except Exception:
    print("kuch to lafda hai")
else:
    print(f.read())

finally:
    print("finnaly to dono hee case, me print hoga")
