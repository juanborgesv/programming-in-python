menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

# Map
map_coffee = map(find_coffee, menu)
print(map_coffee) # Prints a map object but not its actual content.
print('\nThe coffees that start with the letter c are: ')
for x in map_coffee:
    print(x)

# Filter
filter_coffee = filter(find_coffee, menu)
print(filter_coffee) # Prints a filter object but not its actual content.
print('\nThe coffees that start with the letter c are: ')
for x in filter_coffee:
    print(x)

# Difference between Map and Filter is that a Map modifies the values, while
# filter modifies the list.