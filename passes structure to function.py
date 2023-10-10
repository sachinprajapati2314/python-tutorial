# in python
def sachin():
   pass

# in c 
class person:
    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department
infor_in = input("enter the name, age, salary and department = ")
infor_in1 = input()
infor_in2 = input()
infor_in3 = input()


p = person(infor_in,infor_in1,infor_in2,infor_in3)

print("Name : ",p.name)
print("Age : ",p.age)
print("Salary : ",p.salary)
print("Department : ",p.department)
