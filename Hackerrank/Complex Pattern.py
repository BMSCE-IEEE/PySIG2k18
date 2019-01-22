# n being half the size of the diamond
# s0, s1 being top and bottom half indent of the diamond
# a1, a2 being the internal spacing of top-left and top-right
# a3, a4 being the internal spacing of bottom-left and bottom-right

n = int(input())
s0, s1 = map(int, input().split(" "))
a1, a2, a3, a4 = map(int, input().split(" "))

# Top Half
for i in range(n):
    # Spacing
    print(" " * a1, end="")
    print(" " * (n - i - 1) * s0, end="")
    # Top-Left Triangle
    for j in range(i + 1):
        print("*", end="")
        # Internal Spacing
        if j != i:
            print(" " * a1, end="")
    # Top-Right Triangle
    for j in range(i):
        print(" " * a2, end="")
        print("*", end="")
    print()

# Bottom Half
for i in range(n - 1, -1, -1):
    # Spacing
    print(" " * a3, end="")
    print(" " * (n - i) * s1, end="")
    # Bottom-Left Triangle
    for j in range(i):
        print("*", end="")
        if j != i - 1:
            print(" " * a3, end="")
    # Bottom-Right Triangle
    for j in range(i - 1):
        print(" " * a4, end="")
        print("*", end="")
    print()
