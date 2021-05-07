#!/usr/bin/python3
def roman_to_int(roman_string):
    num, i = 0, 0
    romus = {
        'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1
    }

    if type(roman_string) != str or roman_string is None:
        return num

    while i < len(roman_string):
        if i + 1 < len(roman_string) and \
           romus[roman_string[i]] < romus[roman_string[i + 1]]:
            num += romus[roman_string[i + 1]] - romus[roman_string[i]]
            i += 2
        else:
            num += romus[roman_string[i]]
            i += 1

    return num
