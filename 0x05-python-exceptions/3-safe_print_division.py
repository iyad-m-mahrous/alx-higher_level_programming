#!/usr/bin/python3

def safe_print_division(a, b):
    '''divides 2 integers and prints the result.
    Args:
        a and b are integers

    Return:
        the value of the division, otherwise: None
    '''
    result = 0.0
    try:
        result = (a/b)
    except (ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
