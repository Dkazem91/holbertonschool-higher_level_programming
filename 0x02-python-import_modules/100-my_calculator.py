#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = len(sys.argv)
    if(args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    operator = sys.argv[2]
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if(operator in "+-*/"):
        if operator is "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif operator is "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif operator is "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        else:
            print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
