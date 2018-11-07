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

# A little about built in sort


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
        if i != 1:
            average = ((average * (i - 1)) + (bubble_sort_time/start_time)) / i
            print(average)
    # My results:
    # 22300 times faster for 10000
    # 2600 times faster for 1000
    # 210 times faster for 100 values
    # 17 times faster for 10 values


if __name__ == '__main__':
    main()