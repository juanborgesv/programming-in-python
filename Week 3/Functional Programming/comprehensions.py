# =============================================================================
# Part I: List comprehension
print("\nPART I:")
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]

# Get even numbers 
even = [x for x in numbers if x % 2 == 0]
print('Even numbers: ', even)

# Get numbers with cero in them.
cero_in_numbers = [x for x in range(105) if '0' in str(x)]
print('Numbers with 0: ', cero_in_numbers)

big_numbers = [x * 1000 for x in numbers]
print('Big numbers: ', big_numbers)

# =============================================================================
# Part I: Dictionary comprehension
print("\nPART II:")

months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]

# Note: The number '13' is not included since zip will stop when it can't 
# create a tuple from numbers and months.
months_dict = {key:value for (key,value) in zip(numbers, months)}
print('Months: ', months_dict)