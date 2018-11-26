number = int(input())
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
