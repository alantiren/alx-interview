#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    skip = 0
    n = len(data)

    for i in range(n):
        if skip > 0:
            skip -= 1
            continue

        if type(data[i]) != int or data[i] < 0 or data[i] > 0x10ffff:
            return False

        if data[i] <= 0x7f:
            continue

        if (data[i] & 0b11111000) == 0b11110000:
            span = 4
        elif (data[i] & 0b11110000) == 0b11100000:
            span = 3
        elif (data[i] & 0b11100000) == 0b11000000:
            span = 2
        else:
            return False

        if n - i >= span and all((data[j] & 0b11000000) == 0b10000000 for j in range(i + 1, i + span)):
            skip = span - 1
        else:
            return False

    return True
