# write a method 'salaryafterincrement' method with a @property decorator with a setter which changes the value of increment based salary.
#write a method 'salaryafterincrement' method with a @propert decorator with a setter which changes the value of incement based the salary 
class Employee:
    def __init__(self, salary, increment):
        self._salary = salary
        self._increment = increment

    @property
    def salaryafterincrement(self):
        return self._salary * (1 + self._increment)

    @salaryafterincrement.setter
    def salaryafterincrement(self, new_increment):
        self._increment = new_increment

# Example usage
emp = Employee(50000, 0.10)
print("Salary after increment:", emp.salaryafterincrement)

# Changing the increment
emp.salaryafterincrement = 0.20
print("Salary after new increment:", emp.salaryafterincrement)
