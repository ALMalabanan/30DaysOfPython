# 1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are old enough to drive.")
else:
    print(f"You need {18 - age} more years to learn to drive.")

# 2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age = 25
your_age = int(input("Enter your age: "))
if my_age > your_age:
    age_diff = my_age - your_age
    if age_diff == 1:
        print("I am 1 year older than you.")
    else:
        print(f"I am {age_diff} years older than you.")
elif your_age > my_age:
    age_diff = your_age - my_age
    if age_diff == 1:
        print("You are 1 year older than me.")
    else:
        print(f"You are {age_diff} years older than me.")
else:
    print("We are the same age.")

# Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print(a, "is greater than", b)
elif a < b:
    print(a, "is smaller than", b)
else:
    print(a, "is equal to", b)

