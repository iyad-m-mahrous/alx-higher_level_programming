#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def task6():
    args = sys.argv[1:]
    length = len(args)
    result = 0

    if length != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)

    if args[1] not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        sys.exit(1)

    a = int(args[0])
    b = int(args[2])

    if args[1] == '+':
        result = add(a, b)
    elif args[1] == '-':
        result = sub(a, b)
    elif args[1] == '*':
        result = mul(a, b)
    else:
        result = div(a, b)

    print(f'{args[0]} {args[1]} {args[2]} = {result}')


def main():
    task6()

if __name__ == '__main__':
    main()
