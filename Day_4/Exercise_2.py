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

# Use index to determine the position of the first occurrence of C in Coding For All.
string = 'Coding For All'
print(string.index('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
string = 'Coding For All'
print(string.index('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
string = 'Coding For All People'
print(string.rfind('l'))

# Use rindex to find the position of the last occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))

#Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.rindex('because'))

#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
start = string.find('because')
end = string.rfind('because') + len('because')
print(string[start:end])

#Does ''Coding For All' start with a substring Coding?
string = 'Coding For All'
print(string.startswith('Coding'))

#Does 'Coding For All' end with a substring 'coding'?
string = 'Coding For All'
print(string.endswith('coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
string = '   Coding For All      '
print(string.strip())

#Which one of the following variables return True when we use the method isidentifier():
#30DaysOfPython
#thirty_days_of_python
print("30DaysOfPython".isidentifier())
print("thirty_days_of_python".isidentifier())

#The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(" # ".join(libraries))

# Use the new line escape sequence to separate the following sentences. 'I am enjoying this challenge.'
# I just wonder what is next.
print("I am enjoying this challenge.\nI just wonder what is next.")

# Use tab escape sequence to separate the following sentences. 'Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki'
print("Name\tAge\tCountry\tCity")
print("Asabeneh\t250\tFinland\tHelsinki")

# Use the string formatting method to display the following: 'radius = 10 area = 3.14 * radius ** 2 The area of a circle with radius 10 is 314 meters square.'
radius = 10
area = 3.14 * radius ** 2
print(f"The area of a circle with radius {radius} is {area} meters square.")

#Make the following using string formatting methods: '8 + 6 = 14'
print(f"8 + 6 = {8 + 6}")
print(f"8 - 6 = {8 - 6}")
print(f"8 * 6 = {8 * 6}")
print(f"8 / 6 = {8 / 6}")
print(f"8 % 6 = {8 % 6}")
print(f"8 // 6 = {8 // 6}")
print(f"8 ** 6 = {8 ** 6}")