#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or not roman_string:
        return 0
    roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
            }
    num = 0
    prev = 0
    for i in roman_string:
        num = roman_values[i]
        if prev < num:
            prev = num - prev
        else:
            prev += num
    return prev
