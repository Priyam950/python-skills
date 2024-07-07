# write a program to find the greatest of four number eneterd by the user.
# Initialize an empty list to store the numbers
numbers = []

# Loop to get 4 numbers from the user
for i in range(4):
    num = int(input(f"Enter your number {i+1}: "))
    numbers.append(num)

# Compare the numbers to find the greatest
if numbers[0] > numbers[1] and numbers[0] > numbers[2] and numbers[0] > numbers[3]:
    print(f"The greatest number is: {numbers[0]}")
elif numbers[1] > numbers[0] and numbers[1] > numbers[2] and numbers[1] > numbers[3]:
    print(f"The greatest number is: {numbers[1]}")
elif numbers[2] > numbers[0] and numbers[2] > numbers[1] and numbers[2] > numbers[3]:
    print(f"The greatest number is: {numbers[2]}")
else:
    print(f"The greatest number is: {numbers[3]}")
