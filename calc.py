import sys

expression = sys.argv
operand_1, operand_2 = int(expression[2]), int(expression[3])
operation = expression[1]

if operation == "add":
    result = operand_1 + operand_2
elif operation == "sub":
    result = operand_1 - operand_2
elif operation == "mul":
    result = operand_1 * operand_2
else:
    result = operand_1 / operand_2
    
print(result)
    