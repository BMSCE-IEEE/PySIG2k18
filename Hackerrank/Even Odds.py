integer_list = input().lstrip("[").rstrip("]").split(",")

# In case this was not python, integer datatype can only hold a couple of digits
# It is better to take the last digit in the string to check for even/odd
even, odd = list(), list()
for integer in integer_list:
    if int(integer[-1]) % 2 != 0:
        odd.append(int(integer))
    else:
        even.append(int(integer))

print("EVEN:", even)
print("ODD:", odd)
