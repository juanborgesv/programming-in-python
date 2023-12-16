# =============================================================================
# Part I: File Handling - Reading
print('\nPart I: File Handling - Reading')

with open('Week 2/foo.txt', 'r') as file:
    print(file.readline())

# =============================================================================
# Part II: File Handling - Writing
print('Part II: File Handling - Writing')

with open('Week 2/foo2.txt', 'w') as file:
    file.write('foo2') # Creates the file if it didn't exist.

# =============================================================================
# Part III: File Handling - Writing (Append)
print('\nPart III: File Handling - Writing (Append)')

with open('Week 2/foo2.txt', 'a') as file:
    file.write('\nfoo2')

print('') # End