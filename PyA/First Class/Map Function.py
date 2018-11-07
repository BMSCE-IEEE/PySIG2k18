# Title: Demonstrate the use of map function

# Map: map(function_object, iterable_1, iterable_2... iterable_n)
# Lambda: lambda arguments : expression     any number of arguments is allowed but only one expression


def single_value():
    single = map(float, input("1 Number: (try 1, 1.1 and 123)\n"))
    print("Input: ", single, type(single))

    # type conversion to int from object
    try:
        single_int = int(single)
        print("\n", single_int, type(single_int))
    except TypeError:
        print("\nConverting a object to int throws Type Error.")

    # type conversion to float from object
    try:
        single_float = float(single)
        print("\n", single_float, type(single_float))
    except TypeError:
        print("\nConverting a object to float throws Type Error.")

    # type conversion to str from object
    single_str = str(single)
    print("\n", single_str, type(single_str), "\nNo Error but data cannot be read.")

    # type conversion to bool from object
    single_bool = bool(single)
    print("\n", single_bool, type(single_bool), "\nNo Error but this is always True.\n")

    # Using a for loop to read data in map object.
    try:
        print("Loop 1:")
        for element in single:
            print(element, type(element), "Object has been used here")
    except ValueError:
        print("Using a loop to read float data throws Value Error because it cannot convert '.'")
    print("Notice how elements were read characterwise.")
    print("Loop 2: \n")
    print("Code never reaches here.\nEmpty - No Data.")
    for element in single:
        print(element, type(element), )


def single_iterable():
    # PASSING ONE ITERABLE:
    iter_input = input("Enter 2 Numbers").strip(" ").split(" ")

    # A List is returned, will be taught next class. Lists are iterables too.
    iter1 = map(float, iter_input)
    print(iter1, type(iter1))

    # Using a for loop to read data in map object.
    for element in iter1:
        print(element, type(element))
    print("Notice how elements were not read characterwise.\nFloats do not throw error.\n")


def two_iterables():
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


def multiple_iterables():
    def power_numbers(a, b, c, d):
        return [a, b, c, d]

    # demo with 4 lists acting as iterables
    list1 = [i**1 for i in range(1, 11)]
    list2 = [i**2 for i in range(1, 11)]
    list3 = [i**3 for i in range(1, 11)]
    list4 = [i**4 for i in range(1, 11)]
    example = map(power_numbers, list1, list2, list3, list4)
    example = list(example)
    print(example, '\n')
    for i in example:
        print(i)


def main():
    while True:
        selection = input("\n1. Single Value.\n2. Single Iterable.\n3. Two Iterables.\n4. Multiple Iterables.\n0. Exit.\n")
        print()
        if selection == "0":
            return
        elif selection == "1":
            single_value()
        elif selection == "2":
            single_iterable()
        elif selection == "3":
            two_iterables()
        elif selection == "4":
            multiple_iterables()


if __name__ == '__main__':
    main()