import time
# A list is a sequence of values. They are mutable

# Syntax of list functions:

# list.append(object)
# list.count(object)
# list.extend(iterable)
# list.index(object, start, stop)
# list.pop(index) Default pops the last element
# list.remove(object)
# list.reverse()
# list.sort([reverse=True]) True implies descending order

# list = list.copy()
# Directly doing list = list means both the lists refers to the same memory space

# A little about built in sort

exampleString = "Sphinx of black quartz judge my vow"
exampleString = exampleString.lower()

# Converting a string to list gives a list of all characters
alphabets = list(exampleString)
print(alphabets, len(alphabets))

# Converting a list to set object removes all duplicates
alphabets = set(alphabets)
print(alphabets, len(alphabets))

# Removing space from the list to obtain a list of alphabets
alphabets.remove(' ')
print(alphabets, len(alphabets))
alphabets = list(alphabets)

# Sorting the list in alphabetical order
alphabets.sort()
print(alphabets, len(alphabets))

# Pop without an index removes the last object in the list
print("list.pop()", alphabets.pop())
print(alphabets, len(alphabets))

# Append adds an object to the end of the list
print("list.append()", alphabets.append('z'))
print(alphabets, len(alphabets))

# Reverse just reverses the list
print("list.reverse()")
alphabets.reverse()
print(alphabets, len(alphabets))

# Clear makes it an empty list
alphabets.clear()
print(alphabets, len(alphabets), "\n")


def bubble_sort(test_list):
    start_time = time.time()
    length = len(test_list)
    for i in range(length):

        for j in range(i+1, length):
            if test_list[i] > test_list[j]:
                test_list[i], test_list[j] = test_list[j], test_list[i]
    return time.time() - start_time


def main():
    average = 0
    test = [i for i in range(10000, 0, -1)]
    for i in range(1, 20):
        bubble_sort_time = bubble_sort(test)
        temp = test
        start_time = time.time()
        temp.sort()
        start_time = time.time() - start_time

        # Usually first few runs are extremely inaccurate for benchmarking in this method
        # if i >= 5:
        average = ((average * (i - 1)) + (bubble_sort_time/start_time)) / i
        print(average)

    # My results:
    # 22300 times faster for 10000 values
    # 2600 times faster for 1000 values
    # 210 times faster for 100 values
    # 17 times faster for 10 values


if __name__ == '__main__':
    main()