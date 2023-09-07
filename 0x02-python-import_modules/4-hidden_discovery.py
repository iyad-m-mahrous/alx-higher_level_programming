#!/usr/bin/python3
import hidden_4


def task4():
    names_list = dir(hidden_4)
    for name in names_list:
        if name[:2] != "__":
            print(f'{name}')


def main():
    task4()


if __name__ == '__main__':
    main()
