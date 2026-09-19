class Employee:
    def __init__(self, name , salary):
        self.name = name
        self.salary = salary

employee1 = Employee( "Mithilesh" , 20000)

print(employee1.name)
print(employee1.salary)