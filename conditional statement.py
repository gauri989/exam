# Write a Python program to check the grade of a student based on marks.
# Use conditional statements (if, elif, else) to categorize the marks as follows:
# 90-100: "Grade A"
# 75-89: "Grade B"
# 50-74: "Grade C"
# 35-49: "Grade D"
# Below 35: "Fail"

marks=int(input("enter the marks of student:"))
if(marks>90):
    print("grade A")
elif(marks>75):
    print("grade B")
elif(marks>50):
    print("grade C")
else:
    print("fail")