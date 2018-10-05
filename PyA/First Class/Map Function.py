# Title: Demonstrate the use of map function

# Syntax: map(function_object, iterable1, iterable2... iterable3)

# SINGLE INPUT:

single = map(float, input("1 Number:"))
# try 1, 1.1 and 123

print(single, type(single))

# type conversion to int from object
try:
    single_int = int(single)
    print(single_int, type(single_int))
except TypeError:
    print("Converting a object to int throws Type Error.")

# type conversion to float from object
try:
    single_float = float(single)
    print(single_float, type(single_float))
except TypeError:
    print("Converting a object to float throws Type Error.")

# type conversion to str from object
single_str = str(single)
print(single_str, type(single_str), "No Error but data cannot be read.")

# type conversion to bool from object
single_bool = bool(single)
print(single_bool, type(single_bool), "No Error but this is always True.\n")

# Using a for loop to read data in map object.
try:
    print("Loop 1:")
    for element in single:
        print(element, type(element), "Object has been used here")
except ValueError:
    print("Using a loop to read float data throws Value Error because it cannot convert '.'")
print("Notice how elements were read characterwise.")
print("Loop 2: \n")
for element in single:
    # Code never reaches here
    print(element, type(element), "Empty - No Data")


# PASSING ONE ITERABLE:
iter_input = input("Enter 2 Numbers").strip(" ").split(" ")
# A List is returned, will be taught next class. Lists are iterables too.

iter1 = map(float, iter_input)
print(iter1, type(iter1))

# Using a for loop to read data in map object.
for element in iter1:
    print(element, type(element))

print("Notice how elements were not read characterwise.\nFloats do not throw error.\n")

# PASSING TWO ITERABLES:
iter_input1 = input("Enter 2 Numbers").strip(" ").split(" ")
iter_input2 = input("Enter 2 more Numbers").strip(" ").split(" ")

# saving data to use later
iter_input3 = map(float, iter_input1)
iter_input4 = map(float, iter_input2)

# typical use of map function
sums = map(lambda a, b: a+b, iter_input1, iter_input2)
# lambda will be covered next class. Basically here it returns a+b
print(sums, type(sums))

# Using a for loop to read data in map object.
for element in sums:
    print(element, type(element))
print("Concatenation occured because inputs were taken as strings.\n")

# Using a for loop to read data in map object.
sums = map(lambda a, b: a+b, iter_input3, iter_input4)
for element in sums:
    print(element, type(element))
print("Addition occured because inputs were taken as floats.")