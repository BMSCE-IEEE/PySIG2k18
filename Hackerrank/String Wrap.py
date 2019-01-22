# ABCDEF
# 4
# Output: ABCD EF
string = input()
width = int(input())
num_letters = len(string)
sections = int(num_letters / width)
for i in range(sections):
        print(string[i * width: (i * width) + width])

if sections * width != num_letters:
    print(string[sections * width:])

