#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    prev_value = 0

    for symbol in roman_string[::-1]:
        value = roman_values[symbol]

        # If the previous value is less than the current value, subtract it.
        if prev_value > value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
