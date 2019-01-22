# n being the number of letters and m being number of inequalities
n, m = map(int, input().split(","))
inequalities = list()
for i in range(m):
    temp = input().split('-')
    inequalities.append(temp)

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# We find all possible pairs using n letters -  nC2
pairs = list()
for i in range(n):
    for j in range(i + 1, n):
        temp = letters[i] + letters[j]
        if temp not in pairs:
            pairs.append(temp)

inequal = dict()

for pair in pairs:
    equation = [0] * m
    for j in range(m):
        # We solve the equation for each pair
        # LHS given -1 and RHS given +1 for an existing pair
        if pair[0] in inequalities[j][0]:
            equation[j] -= 1
        elif pair[0] in inequalities[j][1]:
            equation[j] += 1

        if pair[1] in inequalities[j][0]:
            equation[j] -= 1
        elif pair[1] in inequalities[j][1]:
            equation[j] += 1

        # Since we concern ourselves only with qualitative differences
        # -2 is the same as -1 and +2 is the same as +1
        if equation[j] == -2:
            equation[j] = -1
        elif equation[j] == 2:
            equation[j] = 1
    # We Update the dictionary of equations - Pairs satisfying it.
    if tuple(equation) in inequal.keys():
        inequal[tuple(equation)].append(pair)
    else:
        inequal[tuple(equation)] = [pair]

temp = list()
for pairs in inequal.values():
    # We then take equations with the same solution by multiple pairs.
    if len(pairs) > 1:
        for j in range(len(pairs)):
            for k in range(j + 1, len(pairs)):
                s = pairs[j] + "=" + pairs[k]
                temp.append(s)
temp.sort()
for i in temp:
    print(i)

