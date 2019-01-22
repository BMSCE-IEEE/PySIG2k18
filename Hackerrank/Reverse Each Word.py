strings_list = input().split(" ")
for string in strings_list:
    print(string[::-1], end=" ", flush=True)
# When the end is not a new line character, many output streams tend to store
# the output in its buffer so that it may print line wise which is
# significantly faster. By "flushing" we push the output.
