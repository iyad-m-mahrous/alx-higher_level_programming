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

    match args[1]:
        case '+':
            result = add(int(args[0]), int(args[]2))
        case '-':
            result = sub(int(args[0]), int(args[]2))
        case '*':
            result = mul(int(args[0]), int(args[]2))
        case '/':
            result = div(int(args[0]), int(args[]2))

        print(f'{args[0]} {args[1]} {args[2]} = {result}')


def main():
    task6()


if __name__ == '__main__':
    main()
