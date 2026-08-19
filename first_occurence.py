# ==========================================================
# 19_first_occurrence.py
#
# Create:
#
# first_occurrence(numbers, target)
#
# Requirements:
#
# - Return the position of the FIRST occurrence of target.
# - Return None if target doesn't exist.
# - Do NOT use .index()
#
# Example:
#
# [4, 7, 2, 7, 9]
#
# target = 7
# → 1
#
# target = 5
# → None
#
# ==========================================================

numbers = [4, 7, 2, 7, 9]


def first_occurrence(numbers, target):

    for pos, number in enumerate(numbers):
        if number == target:
            return pos

    return False

print(first_occurrence(numbers, 7))