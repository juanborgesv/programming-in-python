# =============================================================================
# Part I: Exceptions (calculation error)
print('\nPart I: Exceptions (calculation error)')
def divide(a, b):
    result = 0

    try:
        result = a / b
    except ZeroDivisionError as e:
        print("Division of {} and {} went wrong, you can't divide by zero. E: {}".format(a, b, e))
    except Exception as e:
        print("Division of {} and {} went wrong. E: {}".format(a, b, e))

    return result

print(divide(0, 0))

# =============================================================================
# Part II: Exceptions (file handling)
print('\nPart II: Exceptions (file handling)')

file_path = 'foo.text'

try:
    with open(file_path, 'r') as file:
        print(file.read())
except FileNotFoundError as e:
    print("File not found at {}. E: {}".format(file_path, e))
except Exception as e:
    print("Something went wrong when opening file. E: ", e)

print('') # END
