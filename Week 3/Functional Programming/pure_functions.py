list = [1,2,3]

# Not a pure function due to global scope access.
def add_to_list(item):
    return list.append(item)

# Pure function; creates a new list fro lst an [item].
# Alternatively, lst.copy() can be used to copy the list and then append item.
def add_to_list_pure(lst, item):
    return lst + [item]

