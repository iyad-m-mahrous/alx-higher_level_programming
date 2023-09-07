#!/usr/bin/python3
import sys


def task3():
    sum = 0
    for args in sys.argv[1:]:
        sum += int(args)
    print(f'{sum}')


def main():
    task3()


if __name__ == '__main__':
    main()
