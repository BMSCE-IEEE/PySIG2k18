# Read the list, remove the brackets, split it at the commas
string_list = input().rstrip(']').lstrip('[').split(',')
num_strings = len(string_list)

# sizes is a dictionary of length of each string in list
sizes = {len(string_list[i]): i for i in range(num_strings)}

# sorting keys, sorts it according to length of strings
keys = list(sizes.keys())
keys.sort(reverse=True)

final_list = list()
# For Hackerrank Answer - uncomment the following lines
# print("[", end="")
for key_index in range(len(keys)):
    # if key_index + 1 == num_strings:
    #     print(string_list[sizes[keys[key_index]]], end="]")
    # else:
    #     print(string_list[sizes[keys[key_index]]], end=",")
    final_list.append(string_list[sizes[keys[key_index]]].strip("\""))
print(final_list)
