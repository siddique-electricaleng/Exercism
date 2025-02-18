"""
Class Outer:
    Class Inner:

Benefits:
1. Allows you to logically group classes that are closely related
2. Encapsulates private details that aren't relevant outside of the outer classes (note this isn't encapsulation).
3. Keeps the namespace clean; reduces the possibility of naming conflicts
"""

# Here each of the Employees classes can have different attributes and methods depending on where they belong

""" 
class Company:
    class Employee:
        print("This is the first class")


class Nonprofit:
    class Employee:
        print("This is the second class")
"""


class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position

        def get_details(self):
            return f"{self.name} --> {self.position}"

    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = []

    def add_employee(self, name, position):
        # Create an object
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)

    def list_employees(self):
        return [employee.get_details() for employee in self.employees]


company1 = Company("Under the Sea")
print(company1.company_name)
company1.add_employee("Eugene", "Manager")
company1.add_employee("Spongebob", "Cook")
company1.add_employee("Squidward", "Cashier")
for employee_pos in company1.list_employees():
    print(employee_pos)


company2 = Company("Chum Bucket")
print(company2.company_name)
company2.add_employee("Sheldon", "Manager")
company2.add_employee("Karen", "Assistant")

for employee_pos in company2.list_employees():
    print(employee_pos)
