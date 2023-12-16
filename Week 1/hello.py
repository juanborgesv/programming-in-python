# =============================================================================
# Part I: printing strings, variables and the use of methods.
print("\nPART I:")

# Addition of two variables.
def add(x, y):
    return x+y

# Print initial hello message.
print("Hello, good luck on your python learning journey.")

# Declaring two number variables to test the sum of both.
a, b = 1, 2
x = y = 10

# Print the addition of two numbers.
print(f"Adding the numbers {a} and {b} results in {str(add(a, b))}.")
print(f"Adding the numbers {x} and {y} results in {str(add(x, y))}.")

# Testing '\' which adds the following line to the current one. Additionally, 
# testing different single and double quotes to show when it's appropiate to
# use each.
print("You're " \
      "very smart!" \
        ' Remember to say it out loud "I AM VERY SMART".')

# Deleting various variables.
del a, b, x, y

# =============================================================================
# Part II: Data types.
print("\n\nPART II:")

# List data structure which contains a list of names.
names = ["Juan", "Alejandro"]
names.append("Borges")
print(f'The data type of the collection "names" is {type(names)} and its ' \
      f'first value is "{names[0]}" and the last is {names[-1]}.')

# Tuple; a list that can't be modified.
last_names = ("Garcia", "Marquez")
print(f'The data type of the collection "last_names" is {type(last_names)}' \
      ' and its values are {} and {}.'.format(last_names[0], last_names[1]))

# Dictionary; key-value pair collection.
students = {
    'Andres' : 71,
    'Luis' : 56
}
print('We have a total of {} students in the students collection ({}).' \
      .format(len(students), type(students)))

# Set; unordered collection of unique values.
numbers = {1, 2, 3, 1}

# =============================================================================
# Part III: Input.
print("\n\nPART III:")

# Reads inputs that represent the values of math and physics grades.
math_grade = float(input("Mathematics Grade: "))
phy_grade = float(input("Physics grade: "))

# Prints the me
print("Mean: {}".format((math_grade + phy_grade) / 2))