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

# 2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn.
# December, January or February, the season is Winter.
# March, April or May, the season is Spring
# June, July or August, the season is Summer
season = input("Enter the month: ").capitalize()
if season in ['September', 'October', 'November']:
    print("The season is Autumn.")
elif season in ['December', 'January', 'February']:
    print("The season is Winter.")
elif season in ['March', 'April', 'May']:
    print("The season is Spring.")
elif season in ['June', 'July', 'August']:
    print("The season is Summer.")
else:
    print("Invalid month entered.")

# 3. The following list contains some fruits:
# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input("Enter a fruit name: ").lower()
if new_fruit in fruits:
    print("That fruit already exists in the list.")
else:
    fruits.append(new_fruit)
    print("Modified list:", fruits)