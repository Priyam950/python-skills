# write a program using function to convert celsiuis to fahrenheit
def f_to_c(f):
    return 5*(f-32)/9
f = int(input("enter temperature in f: "))
print(f"{round(f_to_c(f),2)} degree celsius")