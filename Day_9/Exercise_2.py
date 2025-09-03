# 1. Write a code which gives grade to students according to theirs scores:
score = int(input("Enter your score: "))
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print(f"Your grade is {grade}")