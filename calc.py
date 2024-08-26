import sys

operation = sys.argv
num1,num2 =int(operation[2]),int(operation[3])
if operation[1] == "add":
    result = num1+num2
elif operation[1] == "sub":
    result = num1-num2
elif operation[1] == "mul":
    result = num1*num2
else:
    result = num1/num2
print(result)
    