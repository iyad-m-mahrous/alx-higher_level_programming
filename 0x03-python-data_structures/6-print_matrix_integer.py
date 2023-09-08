#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in i[:-1]:
            print('{} '.format(j), end='')
        print('{}'.format(i[-1]))
