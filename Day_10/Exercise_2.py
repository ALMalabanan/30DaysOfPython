# 1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
total_sum = 0
for i in range(101):
    total_sum += i
print("Sum of all numbers from 0 to 100:", total_sum)

# 2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum = 0
odd_sum = 0
for i in range(101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print("Sum of all even numbers from 0 to 100:", even_sum)
print("Sum of all odd numbers from 0 to 100:", odd_sum)