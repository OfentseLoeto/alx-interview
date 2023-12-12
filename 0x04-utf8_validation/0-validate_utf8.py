#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid
UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing 1 byte of data each.
    :return: True if data is a valid UTF-8 encoding, else False.
    """
    # Helper function to check if the given byte is a valid start of
    # a UTF-8 character
    def is_start_of_char(byte):
        return (
            (byte >> 7) == 0 or
            (byte >> 5) == 0b110 or
            (byte >> 4) == 0b1110 or
            (byte >> 3) == 0b11110
        )

    # Helper function to check if the given byte is a continuation byte
    def is_continuation(byte):
        return (byte >> 6) == 0b10

    # Iterate through the data
    i = 0
    while i < len(data):
        if not is_start_of_char(data[i]):
            return False

        char_size = 1
        if (data[i] >> 5) == 0b110:
            char_size = 2
        elif (data[i] >> 4) == 0b1110:
            char_size = 3
        elif (data[i] >> 3) == 0b11110:
            char_size = 4

        # Check if there are enough bytes in the data for the character
        if i + char_size > len(data):
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(i + 1, i + char_size):
            if not is_continuation(data[j]):
                return False

        i += char_size

    return True
