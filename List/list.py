# LISTS IN PYTHON 

marks = [87, 64, 33, 95, 76  , 'William' ,True]
print(marks)
print(type(marks))
print(marks[0])
print(marks[3])
print(marks[5])
print(marks[6])

#NEGATIVE INDEXING EX

colors = ['blue', 'green', 'red', 'yellow', 'white']
print(colors[-3])
print(colors[-1])
print(colors[-5])

# Jump index

age = [3,5,6,12,18,95,7,53,46,20,27]
print(age[1:8])
print(age[1:8:2])

#LIST COMPERHENSION

lst = [i for i in range(4)]
print(lst)   #output:- [0, 1, 2, 3]
lst = [i*i for i in range(4) if i%2==0]
print(lst)