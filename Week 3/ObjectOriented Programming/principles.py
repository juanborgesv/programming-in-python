# Encapsulation
class Person:
    def __init__(self):
        self.name = "Juan"      # Public member.
        self._weight = 79       # Protected member.
        self._height = 185      # Protected member.
        self.__age = 99         # Private member.

# Polymorphism; objects with many forms with its own
# procedures for the + operator.
num_a, num_b = 7, 8
str_a, str_b = 'Juan', 'Borges'
print('{} + {} = {}'.format(num_a, num_b, num_a + num_b))
print('{} + {} = {}'.format(str_a, str_b, str_a + str_b))

# Inheritance
class Pet:
    def __init__(self):
        self.name = ''

class Dog(Pet):
    def __init__(self):
        super().__init__() # Parent constructor.
        self.breed = ''

# Abstraction
from abc import ABC

class Activity(ABC):
    pass    # Abstract class.