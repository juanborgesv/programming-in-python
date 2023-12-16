# =============================================================================
# Part I: Logical operators and control flow
print("\nPART I:")

# Print silly messages using logical operators.
goat = "Messi"
print(f'Is Messi the GOAT? \n - {goat == "Messi"}')

print(f'Is Messi the GOAT and is married? \n - {goat == "Messi" and True}')

# Print a message based on your age.
age = int(input("Enter your age: "))
if age < 13:
    print("You are a kid!")
elif age < 18:
    print("You are a teenager!")
else:
    print("You are an adult!")

# Print a message based on http status code message.
http_status = 200
match http_status:
    case 200 | 201:
        print('Success')
    case 400:
        print('Not found')
    case 500 | 501:
        print('Server error')
    case _:
        print('Unknown!')

# =============================================================================
# Part II: Loops
print("\nPART II:")

# Definition the list of grades and iteration over the collection to get the
# accumulative grade.
grades = [19, 15, 18, 16]
accum = 0
for grade in grades:
    accum += grade

# Print the mean of the grades.
print(f'Your final grade is {accum / len(grades)}')

i = 3 # Iteration ref.

print('Countdown started.')
while (i >= 0):
    print(i)
    i -= 1
print('Countdown ended.')

nums = [1, 2, 3, 4, 5]
for x, num in enumerate (nums):
    if num == 3:
        print('Number 3 found at {}'.format(x))
        break
