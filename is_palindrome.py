# ==========================================================
# 15_is_palindrome.py
#
# Create:
#
# is_palindrome(sequence)
#
# Requirements:
#
# - Return True if the sequence reads the same forwards
#   and backwards.
# - Return False otherwise.
# - Do NOT use reversed()
# - Do NOT create a reversed copy.
# - Use positional/state-based reasoning.
#
# Examples:
#
# [1, 2, 3, 2, 1] → True
# [1, 2, 3, 4, 1] → False
# ["a", "b", "b", "a"] → True
#
# ==========================================================

numbers = [1, 2, 3, 2, 1]


def is_palindrome(sequence):
    left = 0
    right = len(sequence) - 1

    while left < right:
        if sequence[left] == sequence[right]:
            left += 1
            right -= 1

        else:
            return "Not a palindrome"
        
    return "It is a palindrome"


print(is_palindrome(numbers))

