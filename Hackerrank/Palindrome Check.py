number = int(input())


def reverse_method():
    global number
    reverse = 0
    temp = number
    while temp != 0:
        reverse *= 10
        reverse += temp % 10
        temp = int(temp/10)
    if number == reverse:
        print("YES")
    else:
        print("NO")
    

def check_opposite_ends_method():
    global number
    number = str(number)
    half_length = int(len(number) / 2)
    for i in range(half_length):
        if number[i] != number[-1 * (i + 1)]:
            print("NO")
            return
    print("YES")


reverse_method()
check_opposite_ends_method()