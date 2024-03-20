'''
create a class employee with the following attributes:
    name
    age
    identity number
    department

print employee details
 age name and department
'''
class Employee:
    def __init__(self, name, age, id, department):
        self.name = name
        self.age = age
        self.id = id
        self.department = department

    def print_employee_details(self):
        print(f"Name: {self.name}\nID: {self.id}\nAge: {self.age}\nDepartment: {self.department}")

if __name__ == "__main__":
    emp = Employee("John", 25, 1234, "IT")
    emp.print_employee_details()