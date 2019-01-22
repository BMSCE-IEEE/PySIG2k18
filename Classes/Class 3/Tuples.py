# Tuples are a sequence of values. They are Immutable.
# Tuples are work faster than lists.
# Hence are used in places where objects need to be immutable like dictionaries

# Syntax of tuple functions

# integer = tuple.count(object)
# integer = tuple.index(x, start, stop)

example_tuple = tuple([i for i in range(10)])
print(example_tuple)
try:
    print(example_tuple.index(7, 3, 7))
except ValueError:
    print("\nIf element is not present in the tuple or in the specified range. Value Error occurs.\n")

print("tuple.index() ", example_tuple.index(7))

# This is a redeclaration, tuple is still not mutable
example_tuple = (1, 1, 1)
print("tuple.count() ", example_tuple.count(1))
