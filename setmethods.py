# 1. union()/update()
s1 = {1,2,5,6}
s2 = {3,6,7}
print(s1.union(s2))

# 2. intersection()
cities = {"tokyo", "delhi", "madrid", "kabul"}
cities1 = {"madrid", "tokyo", "berlin", "seoul"}
cities2 = cities.intersection(cities1)
print(cities2)

# 3. symmetric_difference()
furits1 = {"apple", "banana", "lichi", "gauva", "mango"}
furits2 = {"grapes", "apple", "mango", "orange", "beery"}
fruits3 = furits1.symmetric_difference(furits2)
print(fruits3)

# 4. difference()
a = {1,3,2,4,5}
b = {3,5,6,2,7}
c = a.difference(b)
print(c)

# 5. isdisjoint()
marks1 = {89, 94, 93, 94, 90}
marks2 = {84, 83, 95, 86, 97}
print(marks1.isdisjoint(marks2))  # True

# 6. superset()
name1 = {"jack", "tom", "elon musk", "harry"}
name2 = {"tim cook", "jhon", "roman", "jack"}
print(name1.issuperset(name2))                 #False

# 7. add()
no = {911, 100, 102}
no.add(112)           # add a single item
print(no)

# 8. update()
laptop1 = {"dell" , "victus", "hp"}
laptop2 = {"mac", "leveno","asus"}
laptop1.update(laptop2)
print(laptop1)

# 9. pop()
cars = {"bmw", "g wagon", 'porsche', "bentley", "thar"}
item = cars.pop()
print(cars)
print(item)

# 10. remove()
sm = {"youtube", "x", "snapchat", "facebook", "instagram"}
sm.remove("youtube")
print(sm)