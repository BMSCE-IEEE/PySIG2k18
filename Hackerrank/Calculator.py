# Operator Operand1 Operand2
operator, operands = input().split(" ", 1)
operands = map(int, operands.split(" "))
operands = list(operands)

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

