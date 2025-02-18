"""
Class Methods = Allow operations related to the class itself

Take (cls) as the first parameter, which represents the class itself. 
"""


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        # Upon initializing each instance of this class we will increment the following class variable
        Student.count += 1
        Student.total_gpa += gpa
    # INSTANCE METHOD

    def get_info(self):
        return f"{self.name} : {self.gpa}"
    # ClASS METHOD - We will pass a class into this method

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}\nTotal GPA is {cls.total_gpa}"

    @classmethod
    def get_avg_gpa(cls):
        if cls.count == 0:
            return "Average GPA is 0"
        else:
            return f"Average GPA: {cls.total_gpa/cls.count:<.1f}"


student1 = Student("Spongebob", 3.2)
student2 = Student("Sandy", 4.0)
student3 = Student("Patrick", 2.0)

print(Student.get_count())
print(Student.get_avg_gpa())
