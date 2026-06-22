#first covert to list , then perform opperation , again convert it to tuples

countries = ("spain" , "itly" , "india" "england" , "germany")
temp = list(countries)
temp.append("russia")
temp.pop(3)
temp[2] = "finland"
countries = tuple(temp)
print(countries)

#concatination without converting them to list

countries1 = ("pakistan" , "afganistan" , "bangladesh" , "srilanka")
countries2 = ("vietnam", "india" , "china")
southEastAsia = countries1 + countries2
print(southEastAsia)

# tuples methods 
# 1. count()
tuple1 = (0, 1, 2, 3, 2, 4, 2, 3, 3, 2, 3 )
res1 = tuple1.count(3)
print("Count of 3 in tuple1 is :" , res1)

# 2. index()
tuple2 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
res2 = tuple2.index(3)
print(res2)

# 3. len()
tuple3 = (0, 1, 2, 3, 2, 3, 1, 3, 2, 3)
res3 = len(tuple3)
print(res3)