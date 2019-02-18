# Author: K Nitesh Srivats
import re


def check_password(password):
    if 6 <= len(password) <= 14:
        if not re.search("[a-z]", password) \
                or not re.search("[0-9]", password) \
                or not re.search("[A-Z]", password) \
                or not re.search("[$#@]", password) \
                or re.search("[^a-zA-Z0-9$#@]", password):
            return False
        else:
            return True
    else:
        return False


def get_json():
    file = open("Data.csv")
    # Stage: Semester: Class: Topic: Grade: [Password, Birth Place]
    json = dict()
    for line in file:
        line = line.split(",")
        if check_password(line[-2]):
            try:
                json[line[0]]
            except KeyError:
                json[line[0]] = dict()
            try:
                json[line[0]][line[1]]
            except KeyError:
                json[line[0]][line[1]] = dict()
            try:
                json[line[0]][line[1]][line[2]]
            except KeyError:
                json[line[0]][line[1]][line[2]] = dict()
            try:
                json[line[0]][line[1]][line[2]][line[3]]
            except KeyError:
                json[line[0]][line[1]][line[2]][line[3]] = dict()
            try:
                json[line[0]][line[1]][line[2]][line[3]][line[4]]
            except KeyError:
                json[line[0]][line[1]][line[2]][line[3]][line[4]] = list()
            json[line[0]][line[1]][line[2]][line[3]][line[4]].append(
                [line[5], line[6]])

    print(json)


if __name__ == "__main__":
    get_json()
