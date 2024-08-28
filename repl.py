from calc import calc_expression
import sys

def main():
    while True:
        user_input = input("Enter the expression: ").split()
        if user_input[0] == "break":
            break
        else:
            result = calc_expression(user_input)
            print(result)

if __name__ == "__main__":
    main()