# write a program to find out whether a given post is talking about "harry" or not.
post = input("enter here :")
if("harry".lower() in post.lower()):
    print("present")
else:
    print("absent")