# =============================================================================
# Part I: Lists
print('\nPart I: Lists')

# List of grades.
grades = [1, 4, 3, 2, 5]
print(grades)

# Sorting method in descending order.
grades.sort(reverse=True)
print(grades)

# Pop; extract the last element in the list/stack.
grade_poped = grades.pop()
print('Grades: {} | Element poped: {}'.format(grades, grade_poped))

# Delete the second to last element of the list.
del grades[-2]
print(grades)

# =============================================================================
# Part II: Tuples
print('\nPart II: Tuples')

random_values = 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 12, 30.1

# Prints how many items in the tuple are of value 'Mon'.
print(random_values.count('Mon'))
#print(random_values.index(1)) # ValueError: '1' isn't in the tuple.

# =============================================================================
# Part III: Sets
print('\nPart III: Sets')

months_a = {1, 2, 3, 4, 5, 6, 7}
months_b = {7, 8, 9, 10, 11, 12}

print('Union of sets: {}'.format(months_a | months_b))
print('Intersection of sets: {}'.format(months_a & months_b))
print('Difference between sets: {}'.format(months_a - months_b))

# =============================================================================
# Part IV: Dictionaries.
print('\nPart IV: Dictionaries')

inventory = {'Book': 5, 'Pencil': 2, 'Eraser': 1}
inventory['Pen'] = 2

print('Books available: ', inventory['Book'])