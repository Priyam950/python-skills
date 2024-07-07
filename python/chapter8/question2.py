# write a program to convert inches to cm
def inch_to_cm(inch):
    return inch*2.54
    
n = int(input("enter the number here"))
print(f"after converting : {inch_to_cm(n)}")