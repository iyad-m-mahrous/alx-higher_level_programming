#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    keys = list(a_dictionary.keys())
    [a_dictionary.pop(i) for i in keys if a_dictionary[i] == value]
    return a_dictionary
