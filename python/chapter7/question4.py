# write  program to find the whether a given number is prime or not.
n = int(input("enter your number here : "))
for i in range(2,n):
   if(n%i)==0:
      print("non prime number")
      break
else:
   print("prime")