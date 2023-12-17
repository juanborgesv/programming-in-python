# =============================================================================
# Part I: Functions
print('\nPart I: ')

# Calculate bill's tax rounded to two decimals.
def get_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

bill = 175.33
tax_rate = 22

print('Total tax: ', get_tax(bill, tax_rate))

# =============================================================================
# Part II: Scope
print('\nPart II: ')

# Global int variable.
global_grade = 15

# Foo 1
def foo1():
    # Enclosed int variable.
    enclosed_grade = 20

    # Foo 1.2
    def foo1p2():
        # Local int variable.
        local_grade = 10

        print('Access to global ', global_grade)
        print('Access to enclosed ', enclosed_grade)

#print(local_grade) # Error. local_grade not defined in print's scope.