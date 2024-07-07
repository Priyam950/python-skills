# write a program to generate multiplication tables from2 to 20 and write it to the different files. place these files in a folder for a 13-year old
import os

# Create a folder named 'MultiplicationTables' if it doesn't exist
folder_name = "MultiplicationTables"
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Function to generate and write multiplication table to a file
def write_multiplication_table(number):
    file_name = f"{folder_name}/table_of_{number}.txt"
    with open(file_name, 'w') as file:
        for i in range(1, 11):
            result = number * i
            file.write(f"{number} x {i} = {result}\n")

# Generate and write multiplication tables from 2 to 20
for num in range(2, 21):
    write_multiplication_table(num)

print("Multiplication tables from 2 to 20 have been written to the folder 'MultiplicationTables'.")
