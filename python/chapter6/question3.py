# A spam comment is defined as a text containig foolowing keywords:
# "Make a lot of money", "buy know","subscribe this","click this". write a program to detect these spams
# List of spam keywords
spam_keywords = ["make a lot of money", "buy now", "subscribe this", "click this"]

# Input from the user
comment = input("Enter your comment: ")

# Check for spam
spam = any(keyword in comment for keyword in spam_keywords)

# Output result
if spam:
    print("This comment is spam.")
else:
    print("This comment is not spam.")
