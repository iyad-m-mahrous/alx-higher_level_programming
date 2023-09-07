#!/usr/bin/python3
import sys


def task2():
    length = len(sys.argv) - 1
    count = 0
    if length == 0:
        print('0 arguments.')
    else:
        print(f'{length} arguments:')
        for args in sys.argv[1:]:
            count += 1
            print(f'{count}: {args}')


def main():
    task2()


if __name__ == '__main__':
    main()
