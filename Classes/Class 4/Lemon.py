import math
# The Solution is a modified binary search
# Worst case is for the last element or in this case index
n, m, s = map(int, input().split(" "))
beg = 1
sum = 0
mid = math.ceil((n + beg) / 2)

while beg <= n:
    # Go to Middle
    mid = math.ceil((n + beg) / 2)
    # We add the minutes it takes to move from one well to middle well(m * ...)
    # Then we add the minutes it takes to check the well(s)
    sum += int((math.fabs(mid - beg)) * m) + s
    if mid == n:
        break
    else:
        beg = mid

print(sum)
