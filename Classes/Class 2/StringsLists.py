exampleString = "Sphinx of black quartz, judge my vow."

print(exampleString)
exampleString = exampleString.title()
print("str.title()", exampleString)
# Similarly str.upper(), str.lower(), str.swapcase(), str.capitalize()


exampleString = "..Sphinx of black quartz,,, judge my vow."
print("\n", exampleString)
# removes chars at the right end of the string
print("str.rstrip(chars)", exampleString.rstrip('.'))
# removes chars at the left end of the string
print("str.lstrip(chars)", exampleString.lstrip('.'))
# removes chars at the both ends of the string
print("str.strip(chars)", exampleString.strip('.'), "\n")

# Returns an Integer
print("str.count(chars, __start, __end)", exampleString.count('.'), "\n")

exampleString = "Sphinx of black quartz, judge my vow."
print(exampleString)
# Returns a Bool
print("str.startswith(prefix, start, end)", exampleString.startswith("Sph"))
print("str.endswith(suffix, start, end)", (exampleString.endswith("vow")), "\n")
print("str.replace(old, new, count)", exampleString.replace(',', ''), "\n")

# ValueError if not found
print("str.index(sub, __start, __end)", exampleString.index('h'))

# Returns -1 if not found
print("str.find(sub, __start, __end)", exampleString.find(';'), "\n")

# Returns a Bool
# str.isalnum() str.isalpha() str.isdecimal() str.isdigit() str.isidentifier()
# str.islower() str.isnumeric() str.isprintable() str.isspace() str.istitle() str.isupper()

# Returns a List
print("str.split(sep, maxsplit)", exampleString.split(" ", 2), "\n", sep="\n")
