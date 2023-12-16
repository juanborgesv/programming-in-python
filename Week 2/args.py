# =============================================================================
# Part II: Args
print('\nPart I: Args')

def sum_of(*args):
    sum = 0

    for x in args:
        sum += x

    return sum

print('The sum of the list of numbers is ', sum_of(1,2,3,4,5,6,7,8,9,10))

# =============================================================================
# Part II: Args
print('\nPart II: Kwargs')

def sum_of_items(**kwargs):
    sum = 0

    for k, v in kwargs.items():
        print('{}: {}$'.format(k, v))
        sum += v

    return sum

print('Total: {}$'.format(sum_of_items(bread=2.99, cake=3.45, juice=1.99)))

print(' ') # End - Additional empty line in console.