#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum_top = 0
    sum_bottom = 0
    for i, j in my_list:
        sum_top += i*j
        sum_bottom += j
    return sum_top / sum_bottom
