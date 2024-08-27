from calc import calc_expression
import sys

def get_cli_input():
    result = calc_expression(sys.argv)
    print(result)

if __name__ == "__main__":
    get_cli_input()