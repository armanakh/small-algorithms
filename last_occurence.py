# ==========================================================
# 20_last_occurrence.py
#
# Create:
#
# last_occurrence(numbers, target)
#
# Requirements:
#
# - Return the position of the LAST occurrence of target.
# - Return None if target doesn't exist.
# - Do NOT use .index()
# - Do NOT use reversed()
#
# Example:
#
# [4, 7, 2, 7, 9]
#
# target = 7
# → 3
#
# target = 5
# → None
#
# ==========================================================

numbers = [4, 7, 2, 7, 9]


def last_occurrence(numbers, target):
    last_pos = None
    for pos, number in enumerate(numbers):
        if number == target:
            last_pos = pos

    return last_pos

print(last_occurrence(numbers, 7))
