# write a pogram to print the multiplication table of a  given number using for loop.
for i in range(3,31,3):
    print(i)

n = int(input("enter your number here :"))
for i in range(1,11):
    print(f"{n}*{i} = {n*i}")