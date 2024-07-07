# write a program to calculate of a given number using for loop
n = int(input("Enter your number here: "))
product = 1

for i in range(1, n + 1):
    product *= i  # Multiply 'product' by 'i' in each iteration

print(f"The factorial of {n} is {product}")
