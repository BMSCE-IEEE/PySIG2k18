# Author: K Nitesh Srivats
import numpy as np

# Just some quick code written for a solution.
# Can be made much more memory and time efficient.
timings = {np.around(a + b * 0.15, decimals=2): None for a in range(24) for b in range(4)}
bookings = {day: timings.copy() for day in range(1, 31)}
n = int(input())


def check(start, end, checkin, checkout):
    for day in range(start, end):
        timings = bookings[day]
        if day == start and day == end - 1:
            for time in range(int(checkin), int(checkout) + 1):
                if time == int(checkin):
                    minutes = np.around(checkin % 1, decimals=2)
                else:
                    minutes = 0
                if time == int(checkout):
                    out = np.around(checkout % 1 + 0.15, decimals=2)
                else:
                    out = 0.6
                while minutes < out:
                    if timings[minutes] is not None:
                        return False
                    minutes = np.around(minutes + 0.15, decimals=2)
        elif day == start:
            for time in range(int(checkin), 24):
                if time == int(checkin):
                    minutes = np.around(checkin % 1, decimals=2)
                else:
                    minutes = 0
                while minutes < 0.6:
                    if timings[minutes] is not None:
                        return False
                    minutes = np.around(minutes + 0.15, decimals=2)
        elif day == end - 1:
            for time in range(0, int(checkout) + 1):
                if time == int(checkout):
                    out = np.around(checkout % 1 + 0.15, decimals=2)
                else:
                    out = 0.6
                minutes = 0
                while minutes < out:
                    if timings[minutes] is not None:
                        return False
                    minutes = np.around(minutes + 0.15, decimals=2)
        else:
            for time in range(0, 24):
                minutes = 0
                while minutes < 0.6:
                    if timings[minutes] is not None:
                        return False
                    minutes = np.around(minutes + 0.15, decimals=2)
    return True


def assign_room(start, end, checkin, checkout):
    for day in range(start, end):
        timings = bookings[day]
        if day == start and day == end - 1:
            for time in range(int(checkin), int(checkout) + 1):
                if time == int(checkin):
                    minutes = np.around(checkin % 1, decimals=2)
                else:
                    minutes = 0
                if time == int(checkout):
                    out = checkout % 1 + 0.15
                else:
                    out = 0.6
                while minutes < out:
                    bookings[day][minutes] = 1
                    minutes = np.around(minutes + 0.15, decimals=2)
        elif day == start:
            for time in range(int(checkin), 24):
                if time == int(checkin):
                    minutes = np.around(checkin % 1, decimals=2)
                else:
                    minutes = 0
                while minutes < 0.6:
                    bookings[day][minutes] = 1
                    minutes = np.around(minutes + 0.15, decimals=2)
        elif day == end - 1:
            for time in range(0, int(checkout) + 1):
                if time == int(checkout):
                    out = np.around(checkout % 1 + 0.15, decimals=2)
                else:
                    out = 0.6
                minutes = 0
                while minutes < out:
                    bookings[day][minutes] = 1
                    minutes = np.around(minutes + 0.15, decimals=2)
        else:
            for time in range(0, 24):
                minutes = 0
                while minutes < 0.6:
                    bookings[day][minutes] = 1
                    minutes = np.around(minutes + 0.15, decimals=2)


def main():
    for i in range(n):
        start, end, checkin, checkout = map(float, input().split(", "))
        start = int(start)
        end = int(end)
        checkin = np.around(checkin, decimals=2)
        checkout = np.around(checkout, decimals=2)
        if check(start, end, checkin, checkout):
            assign_room(start, end, checkin, checkout)
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    main()

