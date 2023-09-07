#!/usr/bin/python3

def magic_calculation(a, b):
    add = getattr(importlib.import_module("magic_calculation_102"), "add")
    sub = getattr(importlib.import_module("magic_calculation_102"), "sub")

    if a < b:
        c = add(a, b)
        for i in range(4, 7):
            c = add(c, i)
    else:
        c = sub(a, b)

    return c
