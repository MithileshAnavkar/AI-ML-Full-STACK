class Employee:
    company = "Google"

    def __init__(self, name):
        self.name = name

employee = Employee("Mithilesh")

print(employee.name)
print(employee.company)