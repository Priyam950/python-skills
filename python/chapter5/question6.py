# create an empty dictionary. Allow 4 friends to enter their favorite languange as value and use keys as their names. Assume that the names are unique

d = {}
for i in range(4):
    name = input(f"enter your name {i+1}:")
    languange = input(f"enter your favourite languange {i+1} :")
    d.update({name:languange})
print(d)
