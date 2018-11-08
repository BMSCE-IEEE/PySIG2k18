# Title : Data types and Basic Input/Output

# Syntax Rules: Anything within square braces is optional

# Input:  variable_name = input([prompt])                           It Always returns a string
# Output: print([values], [sep=' '], [end='\n'])                    Parameters can only be strings

print("A", "B", "Notice the Space")
print("This", "Is", "In", "A", "New", "Line", sep="_")
print("Example - 1", end="")
print("Example - 2.\n")

x = input("Enter a Number: (Try 1, 0, 11.1 and -1.\n")
print("\nInput: ", x, "Type: ", type(x))
print("\nType conversion from string to float.")
x_float = float(x)
print(x_float, type(x_float))

print("\nType conversion from float to integer.")
x_int = int(x_float)
print(x_int, type(x_int))

try:
    print("\nType conversion from string to integer.")
    x_int = int(x)
    print(x_int, type(x_int))

except ValueError:
    print("\nConverting a float value from str to int throws Value Error.")

print("\nType conversion from float to string.")
x_str = str(x_float)
print(x_str, type(x_str))

print("\nType conversion from float to bool.")
x_bool = bool(x_float)
print(x_bool, type(x_bool))

print("\nType conversion from string to bool.")
x_bool = bool(x_str)
print(x_bool, type(x_bool), "Notice how this is always true.")

