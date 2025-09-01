# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# 1. Find the length of the set it_companies
print('Length of IT companies:', len(it_companies))

# 2.  Add 'Twitter' to it_companies
it_companies.add('Twitter')
print('Updated IT companies:', it_companies)

# 3. Insert multiple IT companies at once to the set it_companies
it_companies.update(['Netflix', 'Tesla', 'SpaceX'])
print('IT companies after adding multiple:', it_companies)

# 4. Remove one of the companies from the set it_companies
it_companies.remove('IBM')
print('IT companies after removal:', it_companies)

# 5. What is the difference between remove and discard
# The remove() method will raise an error if the item to remove does not exist, while the discard() method will not.
# Example:
it_companies.discard('IBM')  # This will not raise an error even if 'IBM' is not in the set
print('IT companies after discard:', it_companies)