# ==========================================================
# 16_is_sorted.py
#
# Create:
#
# is_sorted(numbers)
#
# Requirements:
#
# - Return True if the sequence is in ascending order.
# - Return False if any element is greater than the element
#   immediately after it.
# - Do NOT use sorted()
# - Do NOT create another list.
#
# Examples:
#
# [1, 2, 3, 4, 5] → True
# [1, 2, 4, 3, 5] → False
# [5, 4, 3, 2, 1] → False
# [1] → True
#
# ==========================================================

numbers = [1, 2, 3, 4, 5]


def is_sorted(numbers):

    for pos in range(len(numbers) - 1):

        if numbers[pos] >= numbers[pos + 1]:
            return False

        return True
    
print(is_sorted(numbers))