# write a program using to find greatest of three numberss.
def greatest(a,b,c):
    if(a>b and a>c):
      return a
    elif(b>a and b>c):
     return b
    else:
     print("c")
numbers = []
for i in range(3):
    n = int(input(f"enter number here {i+1} :"))
    numbers.append(n)
    
print("the greatest number is :",greatest(*numbers))