import sys

def calc_expression(expression):
    operation = expression[0]
    operand_1, operand_2 = int(expression[1]), int(expression[2])

    if operation == "add":
        result = operand_1 + operand_2
    elif operation == "sub":
        result = operand_1 - operand_2
    elif operation == "mul":
        result = operand_1 * operand_2
    else:
        result = operand_1 / operand_2

    return result
