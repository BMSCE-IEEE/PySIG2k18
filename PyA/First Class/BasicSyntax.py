# Syntax Rules: Anything within square braces is optional

# Input:  variable_name = input([prompt])                           It Always returns a string
# Output: print([values], [sep=' '], [end='\n'])                    Parameters can only be strings
# Range:  range([inclusive_beginning=0], exclusive_end, [skip=1])   Parameters can only be integers

example_string = "Hello"
example_integer = 10
example_float = 0.3
example_float_expo = 3e-1
example_bool = True


# Data types:
def data_types():
    print(example_string, type(example_string))
    print(example_integer, type(example_integer))
    print(example_float_expo, type(example_float))
    print(example_float, type(example_float_expo))
    print(example_bool, type(example_bool))


# Type casting:
def type_casting():
    # Notice the usage of global
    global example_string, example_integer, example_float, example_float_expo, example_bool
    example_string = str(example_string)
    example_integer = int(example_integer)
    example_float = float(example_float)
    example_float_expo = float(example_float_expo)
    example_bool = bool(example_bool)
    data_types()


# Input/Output:
def input_output():
    input_example = input("\nEnter a Number")
    print(input_example, type(input_example))
    print("Input " + input_example + ' Example ' + str(example_integer))
    print("Sum of example and input:", example_integer+int(input_example))


# For Loops:
def for_loops():
    print("\nExample for Loop 1:")
    for number in range(5):
        print(number)
    print("\nExample for Loop 2:")
    for number in range(5, 2, -1):
        print(number)
    print("\nExample for Loop 3:")
    for number in range(2, 5):
        print(number)
    print("\nExample for Loop 4:")
    for number in range(2, 5, 2):
        print(number)
    print("\nExample for Loop 5:")
    for character in example_string:
        print(character)
    print("\nExample for Loop 6:")
    for index_of_character in range(len(example_string)):
        print(example_string[index_of_character], index_of_character)


# While Loop:
def while_loops():
    global example_integer
    print("\nExample while Loop:")
    while example_integer > 6:
        print(example_integer)
        example_integer -= 1
    example_integer = 10

# Operators:
def operators():
    print("\n\nOperators Demo:")
    print("example_integer + 3 =", example_integer + 3)
    print("example_integer - 3 =", example_integer - 3)
    print("example_integer * 3 =", example_integer * 3)
    print("example_integer / 3 =", example_integer / 3)
    print("example_integer // 3 =", example_integer // 3)
    print("example_integer ** 3 =", example_integer ** 3)


def main():
    while True:
        selection = input("\n1. Data Types.\n2. Type Casting.\n3. Input/Output.\n4. For Loops.\n5. While Loops.\n6. Operators.\n0. Exit.\n")
        print()
        if selection == "0":
            return
        elif selection == "1":
            data_types()
        elif selection == "2":
            type_casting()
        elif selection == "3":
            input_output()
        elif selection == "4":
            for_loops()
        elif selection == "5":
            while_loops()
        elif selection == "6":
            operators()


if __name__ == main():
    main()