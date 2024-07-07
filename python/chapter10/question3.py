# write a class "calculator" capableof  finding square,cube abd square root of a number
import math

class Calculator:
    
    # Method to find the square of a number
    def square(self, num):
        return num * num
    
    # Method to find the cube of a number
    def cube(self, num):
        return num * num * num
    
    # Method to find the square root of a number
    def square_root(self, num):
        return math.sqrt(num)

# Example usage
calc = Calculator()

number = int(input("enetr your num : "))
print(f"The square of {number} is: {calc.square(number)}")
print(f"The cube of {number} is: {calc.cube(number)}")
print(f"The square root of {number} is: {calc.square_root(number)}")
