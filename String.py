#Concatenation

str1 = "apna"
str2 = "collage"
final_str = str1 + str2
print(final_str)  #Output : apnacollege

# length of string

str3 = "Python"
len3 = len(str3)
print(len3)  #Output : 6

#Indexing

str4 = "BlackStone"
print(str4[3])  #Output : c

#Slicing

str5 = "ElonMusk"
print(str5[1:5])  #Output : lonM

#StringFunction

str6 = "i am a coder"
print(str6.endswith("er"))  #output : True
print(str6.capitalize())    #output : I am a coder
print(str6.replace("a" , "c"))       #Output : i cm c coder
print(str6.find("d"))          #Output : 9 (index return hota h)
print(str6.count("a"))          #Output : 2