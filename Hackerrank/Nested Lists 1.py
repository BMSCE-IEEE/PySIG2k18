from sys import maxsize
# It is faster to do this question with dictionaries as grades: names

n = int(input())
grades_list = list()
lowest, second_lowest = maxsize, maxsize

# Sorting the entire grade list is expensive, hence search for lowest and
# second lowest giving a max time complexity of O(n) and then sorting the
# list of names which gives a much faster result.
for i in range(n):
    name = input()
    grade = float(input())
    if grade < lowest:
        second_lowest = lowest
        lowest = grade
    grades_list.append([name, grade])

name_list = list()
for grade_pair in grades_list:
    if grade_pair[1] == second_lowest:
        name_list.append(grade_pair[0])

name_list.sort()
for name in name_list:
    print(name)
