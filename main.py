def ask():
    print('calculator application, please give me the ')

    print('1. operand')
    text = input()
    while not text.isnumeric():
        print('bad input, again')
        text = input()
    operand1 = int(text)

    print('operator (+ | - | * | /)')
    text = input()
    while text not in ['+', '-', '*', '/']:
        print('bad input, again')
        text = input()
    operator = text

    print('2. operand')
    text = input()
    while not text.isnumeric():
        print('bad input, again')
        text = input()
    operand2 = int(text)

    return operand1, operator, operand2


def calculate(operand1, p_operator, operand2):
    rv = 0
    if p_operator == '+':
        rv = operand1 + operand2
    elif p_operator == '-':
        rv = operand1 - operand2
    elif p_operator == '*':
        rv = operand1 * operand2
    elif p_operator == '/':
        rv = operand1 / operand2
    return rv


op1, operator, op2 = ask()
result = calculate(op1, operator, op2)
print(f'result: {result}')
exit(0)
