# Program to store seven fruits in a list by the user
fruits = []

# Loop to take seven inputs
for i in range(7):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)

# Print the list of fruits
print("The list of fruits is:", fruits)
