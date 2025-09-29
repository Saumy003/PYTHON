# LIST METHODS

l = [23, 43, 8, 10, 3, 67, 99, 1, 1, 3]
print(l)

l.sort()  #list will sort in asending order
print(l)

l.append(7)  # add 7 at the end of the list
print(l)

print(l.count(10))  # count how many times 10 appers in the list

print(l.index(3))   #display the number which is at the 3rd indexing

m = l.copy()        # copy list l to new list m
m[0] = 0
print(l)

l.insert(1, 999)    # 999 will be  added in the list at first index
print(l)

p = [900, 1000, 1100]
l.extend(p)         # list p will extended and added at the end of list l
print(l)