# Input Section
x_initial, y_initial = map(int, input("Initial Position: ").split(" "))
n = int(input("Moves: "))
x_final, y_final = map(int, input("Final Position: ").split(" "))

# Variables required are declared
visited, temp = list(), list()
found = 0


# Basic functionality required of the question
def new_visited(x, y):
    global visited
    # Finds 8 possible positions
    possible_positions = list()
    possible_positions.append([x - 2, y - 1])
    possible_positions.append([x - 2, y + 1])
    possible_positions.append([x + 2, y - 1])
    possible_positions.append([x + 2, y + 1])
    possible_positions.append([x - 1, y - 2])
    possible_positions.append([x - 1, y + 2])
    possible_positions.append([x + 1, y - 2])
    possible_positions.append([x + 1, y + 2])
    # filters out of bound locations and appends to visited
    visited += list(filter(filter_criteria, possible_positions))


# Accounting for boundary conditions
def filter_criteria(coordinates):
    if 0 <= coordinates[0] <= 8 and 0 <= coordinates[1] <= 8:
        return 1
    else:
        return 0


# Initialization
# Initial Position is the first visited location
visited.append([x_initial, y_initial])

# The Loop
for i in range(n):
    temp = visited.copy()
    visited.clear()
    for coordinate in temp:
        # New possible locations are found from previously visited locations(temp)
        new_visited(coordinate[0], coordinate[1])

# Final Calculations
found = visited.count([x_final, y_final])
print(found*100.0/len(visited), '%')

