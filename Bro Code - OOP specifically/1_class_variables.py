"""
Class Variables:
Shared among all instances of a class
Defined outside the constructor

In the __init__() constructor the variables are instance variables, specific to the instance of the class.

Best to access the class variables by the class name and not by the instance of the class
"""


class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Aela", 20)
student2 = Student("Gorath", 400)
student3 = Student("Liam", 111)
student4 = Student("Tetris", 12)

print(
    f"My graduating class of {Student.class_year} has {Student.num_students} students.")
