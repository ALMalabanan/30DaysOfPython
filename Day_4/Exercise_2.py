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

#Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
string = 'You cannot end a sentence with because because because is a conjunction'
print(string.find('because'))