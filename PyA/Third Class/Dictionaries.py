# A dictionary is like a list. In a list, the index positions have to be integers.
# In a dictionary, the indices can be (almost) any type.
# A dictionary is a mapping between a set of indices(keys) and a set of values. Each key maps to a value.
# The association of a key and a value is called a key-value pair or sometimes an item.

# Searching in a dictionary is O(1) while searching in a list is O(n)

# Dictionary is declared in {}
test = {1: 2, 1: 3, 2: [1], 3: 4, 4: 1, 5: 2}
print(test, "\nFor multiple entries, Latest Values are used.\n")

# To make a new dictionary with the same items
test_copy = test.copy()
print("test_copy: ", test_copy, "\n")

# Clear is used to remove all items in the dictionary
test_copy.clear()
print("after clearing test_copy: ", test_copy, "test: ", test, "\n")

# Get is used to get the value of a key
test[2] = test.get(2) + [1]
print("test after using get: ", test, "\n")

# Keys is used to get the set of all keys
test_keys = test.keys()
print(test_keys, type(test_keys), " Cannot be iterated without converting it to a iterable like list.\n")

# Values is used to get the set of all values
test_values = test.values()
print(test_values, type(test_values), " Cannot be iterated without converting it to a iterable like list.\n")

# Popitem is used to remove the first item in the dictionary
test.popitem()
print("pop items remove the first item in the dictionary: ", test)

# Pop is used to remove an item with a particular key
test.pop(4)
print("After popping key with 4: ", test, "\n")

# To Add elements to a dictionary
test[(10, 20)] = {1: 2, 4: 3}
print(test)

try:
    test[[1, 2]] = 10
except TypeError:
    print("\nDictionary Keys cannot be mutable.")
