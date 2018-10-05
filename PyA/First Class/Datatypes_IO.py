# Title : Data types and Basic Input/Output

# print by default prints a \n in the end.
# syntax: print(values, sep=' ', end='\n')
print("A", "B", "Notice the Space")
print("This", "Is", "In", "A", "New", "Line", sep="_")
print("Example - 1", end="")
print("Example - 2.\n")

# input takes an optional parameter prompt and it always returns a string.
x = input("Enter a Number: ")
# try 10.1, then 6, then 0, then -5.
print(x, type(x))

# type conversion to float
x_float = float(x)
print(x_float, type(x_float))

# type conversion to int from float
x_int = int(x_float)
print(x_int, type(x_int))

try:
    # type conversion to int from str
    x_int = int(x)
    print(x_int, type(x_int))

except ValueError:
    print("Converting a float value from str to int throws Value Error.")

# type conversion to str from float
x_str = str(x_float)
print(x_str, type(x_str))

# type conversion to bool from float
x_bool = bool(x_float)
print(x_bool, type(x_bool))

# type conversion to bool from str
x_bool = bool(x_str)
print(x_bool, type(x_bool), "Notice how this is always true.")

