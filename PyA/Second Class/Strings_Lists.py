exampleString = "Sphinx of black quartz, judge my vow."
a = dir(dict)
for i in a:
    if i[0] != '_':
        print(i)

print("str.upper()", exampleString.upper())
print("str.lower()", exampleString.lower())
print("str.title()", exampleString.title())
print("str.swapcase()", exampleString.title().swapcase())
print("str.capitalize()", exampleString.capitalize())

exampleString = "..Sphinx of black quartz,,, judge my vow."
print("\n\n\n", exampleString)
print("str.rstrip(chars)", exampleString.rstrip('.'))
print("str.lstrip(chars)", exampleString.lstrip('.'))
print("str.strip(chars)", exampleString.strip('.'))

# Returns an Integer
print("str.count(chars, __start, __end)", exampleString.count('.', 3))
print("str.count(chars, __start, __end)", exampleString.count('.', 0, 10))
print("str.count(chars, __start, __end)", exampleString.count('.'))

# Returns a Bool
print("str.startswith(prefix, start, end)", exampleString.startswith(".."))
print("str.endswith(suffix, start, end)", (exampleString.endswith(",,,", 0, 27)))

print("str.replace(old, new, count)", exampleString.replace(',', '', 2))

# ValueError if not found
print("str.index(sub, __start, __end)", exampleString.find(',', 26), exampleString[24:27])

# Returns -1 if not found
print("str.find(sub, __start, __end)", exampleString.find(';'))

# Returns a Bool
ex = "isalnum isalpha isdecimal isdigit isidentifier islower isnumeric isprintable isspace istitle isupper"

# Returns a List
exList = ex.split(" ")
print("str.split(sep, maxsplit)", exList, sep="\n")

exampleString = "Sphinx of black quartz judge my vow"
exampleString = exampleString.lower()
alphabets = list(exampleString)
print(alphabets, len(alphabets))
alphabets = set(alphabets)
print(alphabets, len(alphabets))
alphabets.remove(' ')
print(alphabets, len(alphabets))
alphabets = list(alphabets)
alphabets.sort()
print(alphabets, len(alphabets))

print("list.pop()", alphabets.pop())
print(alphabets, len(alphabets))
print("list.append()")
alphabets.append('z')
print(alphabets, len(alphabets))
print("list.reverse()")
alphabets.reverse()
print(alphabets, len(alphabets))
alphabets.clear()
print(alphabets, len(alphabets))



