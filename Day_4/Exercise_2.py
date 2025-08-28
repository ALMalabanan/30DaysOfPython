# Split the string 'Coding For All' using space as the separator (split()) .
string = 'Coding For All'
print(string.split(" "))

# 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon' split the string at the comma.
string = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
print(string.split(", "))

#What is the character at index 0 in the string Coding For All.
string = 'Coding For All'
print(string[0])

#What is the last index of the string Coding For All.
string = 'Coding For All'
print(string[-1])

#What character is at index 10 in "Coding For All" string.
string = 'Coding For All'
print(string[10])

#Create an acronym or an abbreviation for the name 'Python For Everyone'.
string = 'Python For Everyone'
acronym = ''.join(word[0] for word in string.split())
print(acronym)

#Create an acronym or an abbreviation for the name 'Coding For All'.
string = 'Coding For All'
acronym = ''.join(word[0] for word in string.split())
print(acronym)