class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def __str__(self):
        return f"Name: {self.name}\nID: {self.id}"

class SalaryEmployee(Employee):

    def __init__(self,name,id,salary):
        super().__init__(name,id)
        self.salary = salary
    
    def __str__(self):
        return super().__str__()+f"\nSalary: ${self.salary}"

class CommissionEmployee(SalaryEmployee):
    def __init__(self,name, id, salary, num_sales):
        self.num_sales = num_sales
e = Employee("Earl",7)
s = SalaryEmployee("Sally",34,95000)
print(e)
print(s)