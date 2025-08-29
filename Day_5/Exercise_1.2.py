# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack, then insert Python and SQL after Redux.
full_stack = front_end + back_end
full_stack.insert(full_stack.index('Redux') + 1, 'Python')
full_stack.insert(full_stack.index('Python') + 1, 'SQL')
print(full_stack)