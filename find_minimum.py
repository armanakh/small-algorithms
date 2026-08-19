# ==========================================================
# 17_find_minimum.py
#
# Create:
#
# find_minimum(numbers)
#
# Requirements:
#
# - Return the smallest value in the sequence.
# - Traverse the sequence manually.
# - Do NOT use min()
# - Do NOT sort the sequence.
#
# Example:
#
# [7, 3, 11, 4, 9, 2] → 2
#
# ==========================================================

numbers = [7, 3, 11, 4, 9, 2, 8]


def find_minimum(numbers):
    minimum = numbers[0]

    for number in numbers:
        if number < minimum:
            minimum = number

    return minimum

print(find_minimum(numbers))