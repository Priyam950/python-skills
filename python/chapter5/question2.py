# write a program to input eight numbers from the user and display all the unique numbers (once).
unique_num = set()
for i in range(8):
    num = int(input(f" enter your number here {i+1}:"))
    unique_num.add(num)
    print(unique_num)