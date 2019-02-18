# Author: K Nitesh Srivats
import numpy as np


def path(x, y, dx, dy):
    if solve(x, y, dx, dy):
        print("Solution doesn't exist")
        return
    print(solution)


def solve(x, y, dx, dy):
    if x == dx and y == dy:
        solution[x][y] = 1
        return True
    # course[x][y] == 1 and solution[x][y] == 0
    if 0 <= x < n and 0 <= y < n and course[x][y] and solution[x][y]:
        solution[x][y] = 1
        # Right or Left
        if x < dx:
            if solve(x + 1, y, dx, dy):
                return True
            if solve(x - 1, y, dx, dy):
                return True
        else:
            # Left or Right
            if solve(x - 1, y, dx, dy):
                return True
            if solve(x + 1, y, dx, dy):
                return True

        if y < dy:
            # Up or Down
            if solve(x, y + 1, dx, dy):
                return True
            if solve(x, y - 1, dx, dy):
                return True
        else:
            # Down or Up
            if solve(x, y - 1, dx, dy):
                return True
            if solve(x, y + 1, dx, dy):
                return True
        solution[x][y] = 0
    return False


file = input("Enter Map Name: ")
course = np.load(file)
print(course)
n = len(course[0])
solution = np.zeros((n, n), dtype="int8")
x, y = map(int, input("Enter Start Coordinates: ").split(","))
dx, dy = map(int, input("Enter End Coordinates: ").split(","))
path(x - 1, y - 1, dx - 1, dy - 1)
