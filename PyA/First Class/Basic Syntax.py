# Syntax Rules: Anything within square braces is optional

# Data types:
example_string = "Hello"
print(example_string, type(example_string))
example_integer = 10
print(example_integer, type(example_integer))
example_float_expo = 3e-1
print(example_float_expo, type(example_float_expo))
example_float = 0.3
print(example_float, type(example_float_expo))
example_bool = True
print(example_bool, type(example_bool))

# Type casting:
example_string = str(example_string)
example_integer = int(example_integer)
example_float = float(example_float)
example_float_expo = float(example_float_expo)
example_bool = bool(example_bool)

# Input: variable_name = input([prompt])
# It Always returns a string

# Output: print([values], [sep=' '], [end='\n'])
# print can only print out Strings
input_example = input("\nEnter a Number")
print(input_example, type(input_example))
print(input_example + ' ' + str(example_integer))
print("Sum of example and input:", example_integer+int(input_example))

# for Loops:
# No definite syntax can be defined for for loops

# Types of for loop

print("\nExample for Loop 1:")
for number in range(5):
    print(number)
print()

print("\nExample for Loop 2:")
for number in range(5, 2, -1):
    print(number)
print()

print("\nExample for Loop 3:")
for number in range(2, 5):
    print(number)
print()

print("\nExample for Loop 4:")
for number in range(2, 5, 2):
    print(number)
print()

# Syntax of range([inclusive_beginning=0], exclusive_end, [skip=1])

print("\nExample for Loop 5:")
for character in example_string:
    print(character)
print()

print("\nExample for Loop 6:")
for index_of_character in range(len(example_string)):
    print(example_string[index_of_character], index_of_character)
print()

# while loop:

print("\nExample while Loop:")
while example_integer > 6:
    print(example_integer)
    example_integer -= 1

# if-elif-else:

print("\nExample if-elif-else")

while example_integer < 10:
    print("\nExample", example_integer-5, ":")
    print("example_integer: ", example_integer)
    if example_integer == 6 and example_string == "Hello":
        print("if statement 1")
    elif example_integer < 8 or example_float != 0.3:
        print("elif statement 1")
    elif example_integer == 8 and "ell" in example_string:
        print("elif statement 2")
    else:
        print("else statement 1")
    example_integer += 1

# Operators:
print("\n\nOperators Demo:")
print("example_integer + 3 =", example_integer + 3)
print("example_integer - 3 =", example_integer - 3)
print("example_integer * 3 =", example_integer * 3)
print("example_integer / 3 =", example_integer / 3)
print("example_integer // 3 =", example_integer // 3)
print("example_integer ** 3 =", example_integer ** 3)

