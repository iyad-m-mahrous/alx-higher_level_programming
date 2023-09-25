#!/usr/bin/python3


def magic_calculation(a, b):
    """Performs the same calculation as the given Python bytecode.
    Args:
        a: A number.
        b: A number.

    Returns:
        The result of the calculation.
    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return result
