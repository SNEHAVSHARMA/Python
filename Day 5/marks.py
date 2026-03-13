student_marks=[90,55,44,32,23,47,58,96]
# total=sum(student_marks)        #built-in function
# print(total)

# sum=0
# for marks in student_marks:
#     sum+=marks
# print(sum)                      #function using for loop
               
highest=max(student_marks)
print(highest)

max=0
for marks in student_marks:
    if marks>max:
        max=marks
print(max)
