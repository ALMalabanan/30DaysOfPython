# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
fruits = ['banana', 'orange', 'mango', 'lemon', 'apple', 'grape']

# Find the length of your list
length = len(fruits)
print("Number of fruits:", length)

# Get the first item, the middle item and the last item of the list
first_item = fruits[0]
middle_item = fruits[length // 2]
last_item = fruits[-1]

print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Angelo', 23, 5.7, 'Single', '123 Main St']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(mixed_data_types)
print(it_companies)

# Print the number of companies in the list
print("Number of IT companies:", len(it_companies))

# Print the first, middle and last company
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

# Print the list after modifying one of the companies
it_companies[0] = 'Meta'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Tesla')
print(it_companies)

# Insert an IT company in the middle of the companies list
middle_index = len(it_companies) // 2
it_companies.insert(middle_index, 'Intel')
print(it_companies)

# Change one of the it_companies names to uppercase
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
joined_companies = '#;  '.join(it_companies)
print(joined_companies)

# Check if a certain company exists in the it_companies list.
company_to_check = 'Google'
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
first_three = it_companies[:3]
print(first_three)

# Slice out the last 3 companies from the list
last_three = it_companies[-3:]
print(last_three)

# Slice out the middle company or companies from the list
middle = it_companies[len(it_companies) // 2]
print(middle)

# Remove the first company from the list
it_companies.pop(0)
print(it_companies)

# Remove the middle company or companies from the list
middle_index = len(it_companies) // 2
it_companies.pop(middle_index)
print(it_companies)

# Remove the last company from the list
it_companies.pop()
print(it_companies)

# Remove all companies from the list
it_companies.clear()
print(it_companies)

# Destroy the list
del it_companies