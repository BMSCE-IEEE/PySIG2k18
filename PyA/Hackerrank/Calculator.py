operator, operands = input().split(" ", 1)
operands = map(int, operands.split(" "))
operands = list(operands)
for index in range(len(operands)):
    try:
        operands[index] = int(operands[index])
    except ValueError:
        operands[index] = float(operands[index])
if operator == '+':
    print(operands[0] + operands[1])
elif operator == '-':
    print(operands[0] - operands[1])
elif operator == '*':
    print(operands[0] * operands[1])
elif operator == '/':
    print(operands[0] / operands[1])
elif operator == '%':
    print(operands[0] % operands[1])

