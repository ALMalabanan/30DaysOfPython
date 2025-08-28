# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
first = 'Thirty'
second = 'Days'
third = 'Of'
fourth = 'Python'
result = first + ' ' + second + ' ' + third + ' ' + fourth
print(result) # 'Thirty Days Of Python'

#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
first = 'Coding'
second = 'For'
third = 'All'
result = first + ' ' + second + ' ' + third
print(result) # 'Coding For All'

#Declare a variable named company and assign it to an initial value "Coding For All".
company = 'Gelo D Great'

#Print the variable company using print().
print(company)

#Print the length of the company string using len() method and print().
print(len(company))

#Change all the characters to uppercase letters using upper() method.
print(company.upper())

#Change all the characters to lowercase letters using lower() method.
print(company.lower())

#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

#Cut(slice) out the first word of Company string.
print(company[4:])

# Check if Company string contains a word Gelo using the method index, find or other methods.
print(company.find("Great"))
print(company.index("Great"))

#Replace the word Great in the string 'Gelo D Great' to Python.
print(company.replace("Great", "Python"))

#Change d to is using the replace method or other methods.
print(company.replace("D", "is"))

