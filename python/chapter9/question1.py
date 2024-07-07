# write a program to read the text from agiven file 'poems.txt' and find out whether it contains the word 'twinkle'.
file = open("poems.txt")
poem = file.read()
if("Twinkle" in poem):
    print("presented")
else:
    print("absent")
file.close