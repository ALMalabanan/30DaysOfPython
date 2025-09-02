# Create an empty dictionary called dog
dog = {}

# Add name, color, breed, legs, age to the dog dictionary
dog['name'] = 'Buddy'
dog['color'] = 'Brown'
dog['breed'] = 'Labrador'
dog['legs'] = 4
dog['age'] = 5

# Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student = {
    'first_name': 'John',
    'last_name': 'Doe',
    'gender': 'Male',
    'age': 25,
    'marital_status': 'Single',
    'skills': ['Python', 'JavaScript', 'SQL'],
    'country': 'USA',
    'city': 'New York',
    'address': {
        'street': '123 Main St',
        'zipcode': '10001'
    }
}
 
# Get the length of the student dictionary
length = len(student)
print('Length of student dictionary:', length)

# Get the value of skills and check the data type, it should be a list
skills = student.get('skills', [])
print('Skills:', skills)
print('Type of skills:', type(skills))

# Modify the skills values by adding one or two skills
student['skills'].append('HTML')
student['skills'].append('CSS')
print('Updated skills:', student['skills'])

# Get the dictionary keys as a list
keys = list(student.keys())
print('Keys:', keys)

# Get the dictionary values as a list
values = list(student.values())
print('Values:', values)
