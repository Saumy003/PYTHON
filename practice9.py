# Q1.  Create student class that takes name & marks of 3 subject as argument in constructor .
#  Then crate a method to print the average.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print('Hii', self.name, "your avg score is :", sum/3)

s1 = Student("Tony Stark", [99, 97, 98])
s1.get_avg()

