# ==========================================================
# 13_rotate_right.py
#
# Create:
#
# rotate_right(numbers)
#
# Requirements:
#
# - Move the final element to position 0.
# - Shift every other element one position to the right.
# - Modify the original list.
# - Do not create a second list.
# - Return the modified list.
#
# Example:
#
# [1, 2, 3, 4, 5]
#
# →
#
# [5, 1, 2, 3, 4]
#
# ==========================================================

numbers = [1, 2, 3, 4, 5]


def rotate_right(numbers):
    reverse = len(numbers) - 1
    last = numbers[-1]

    while reverse > 0:
        numbers[reverse] = numbers[reverse - 1]

        reverse -= 1
    numbers[0] = last
    return numbers    
    
print(rotate_right(numbers))

