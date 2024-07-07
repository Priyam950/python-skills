# write a program to find out whether a student has passed or failed if it requiresa total of 40% and at least 33% in each subject has pass. Assume 3 subjects and take marks as an input from the user.
result=[]
for i in range(3):
    marks = int(input(f"enter marks {i+1} :"))
    result.append(marks)
total_marks = sum(result) 
total_percentage = (total_marks/300)*100
if(total_percentage>=40 and all(marks>=33 for mark in result)) :
    print("congratulation! you have pass the exam")  
else:
    print("oops! try again")
