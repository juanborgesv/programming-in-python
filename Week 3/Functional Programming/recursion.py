# =============================================================================
# Part I: Recursion - Factorial
print("\nPART I:")

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

factorial_n = 6
print(f'Factorial of {factorial_n} is {factorial(factorial_n)}')

# =============================================================================
# Part II: Recursion - Palindrome
print("\nPART II:")

def is_palindrome(word):
    return word == word[::-1]

word = 'nun'
print(f'Is "{word}" a palindrome? R: {is_palindrome(word)}')

# =============================================================================
# Part III: Recursion - Reversing word
print("\nPART II:")

def reverse_word(word):
    if (len(word) == 1):
        return word
    else:
        return reverse_word(word[1:]) + word[0]
    
word = 'hello'
print(f'{word} reversed is {reverse_word(word)}')