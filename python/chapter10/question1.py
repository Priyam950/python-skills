# Create a class "Programmer" for storing information of few programmers working at Microsoft.
class programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = programmer("Sujal",1,110044)
print(p.name,p.salary,p.pin)
r = programmer("rohan",1,110044)
print(r.name,r.salary,r.pin)