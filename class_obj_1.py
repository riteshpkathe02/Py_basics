class Employee:
    def __init__(self, id, name):
        self.id=id
        self.name=name
        
    def print_about(self):
        print("Emp_ID: ", self.id)
        print("Emp_Name: ", self.name)

emp = Employee(1,"coder")
emp.print_about()

del emp.id
#Deleting the object itself
try:
    print(emp.id)
except AttributeError:
    print("emp.id is not defined")

del emp
try:
    emp.print_about() #It will gives error after deleting emp
except NameError:
    print("emp is not defined")