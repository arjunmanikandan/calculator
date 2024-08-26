import sys

expression = sys.argv
num1,num2 =int(expression[2]),int(expression[3])
if expression[1] == "add":
    result = num1+num2
elif expression[1] == "sub":
    result = num1-num2
elif expression[1] == "mul":
    result = num1*num2
else:
    result = num1/num2
print(result)
    