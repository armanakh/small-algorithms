# ==========================================================
# 18_find_second_largest.py
#
# Create:
#
# find_second_largest(numbers)
#
# Requirements:
#
# - Return the second-largest DISTINCT value.
# - Traverse the sequence manually.
# - Do NOT use sorted()
# - Do NOT use max()
# - Do NOT create a sorted copy.
#
# Examples:
#
# [7, 3, 11, 4, 9, 2] → 9
#
# [7, 11, 11, 4, 9] → 9
#
# [5, 5, 5] → None
#
# ==========================================================

numbers = [7, 3, 11, 4, 9, 2]

def find_second_largest(numbers):

    highest = numbers[0]
    second_highest = None

    for number in numbers[1:]:

        if number > highest:
            second_highest = highest
            highest = number

        elif number < highest:
            if second_highest is None or number > second_highest:
                second_highest = number

    return second_highest

 

print(find_second_largest(numbers))