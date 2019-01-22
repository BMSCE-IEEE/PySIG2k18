# Regular expressions: Sequence of characters that used for
# searching and parsing strings
# The regular expression library 're' should be imported before you use it

import re

# Metacharacters: characters with special meaning

# '.'  : Any character                                  "b..d"
# '*'  : Zero or more occurrences                       "bal*"
# '+'  : One or more occurrences                        "bal+"
# '^'  : Starts with                                    "^bald"                                  
# '$'  : Ends with                                      "bald$"
# '{}' : Exactly the specified number of occurrences    "al{3}"
# '()' : Capture and group
# '|'  : Either or                                      "bald|ball"
# '\'  : Signals a special sequence                     "\d"

# Special Sequences: A special sequence is a '\' followed by one of the
# characters which has a special meaning

# \d : Returns a match if string contains digits
# \D : Returns a match if string DOES NOT contain digits
# \s : Returns a match for a white space character
# \S : Match for non white space character
# \w : Match for word character(a-z,A-Z,0-9,_)
# \W : Returns a match if it DOES NOT contain word characters


# search function: Searches for first occurrence of pattern within a string.
# Returns a match object if there is a match
# Syntax: re.search(pattern,string)

line = "Message from anjali@gmail.com to nitesh@gmail.com"
mailId = re.search('\S+@\S+', line)
print("The first mail id is at position:", mailId.start())

# If the pattern is not present it returns None
line = "Message from anjali@gmail.com to nitesh@gmail.com @ 3:00"
time = re.search("\d{2}:\d{2}", line)
print(time)
# Returns none as no such pattern

# findall function: Returns a list containing all matches
line = "Message from anjali@gmail.com to nitesh@gmail.com"
mailId = re.findall('\S+@\S+', line)
print(mailId)

# Search for lines that start with From and have an at sign
"""
hand = open('example.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:.+@', line):
        print(line)
"""

# Escape characters: A way to indicate special characters by using backslash
line = "I received $1000 as a scholarship"
amount = re.findall("\$\d{4}", line)
print(amount)
# Since we prefix dollar sign with backslash it matches dollar sign and not
# end of string
