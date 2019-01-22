demo_string = "The quick brown fox jumps over a lazy dog."
demo_string = demo_string.upper()
demo_list = list(demo_string)
demo_list = filter(str.isalpha, demo_list)
demo_list = list(demo_list)
alphabets = dict()

for letter in demo_list:
    # Checking if key exists in dictionary
    if letter in alphabets:
        # If key exists, increase letter count
        alphabets[letter] += 1
    else:
        # Else create a key value pair
        alphabets[letter] = 1
        # this also works - alphabets.update({letter: 1})

# Notice how there is no particular order
# Run this script multiple times, dictionary order always changes
print(alphabets, "\n")

alphabets_list = [[key, alphabets[key]] for key in alphabets]
alphabets_list.sort()
print(alphabets_list)
