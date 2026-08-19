# ==========================================================
# 14_partition.py
#
# Create:
#
# partition(numbers, pivot)
#
# Requirements:
#
# - Modify the original list.
# - Do NOT create a second list.
# - Rearrange the elements so that:
#
#       elements < pivot
#       come before
#       elements >= pivot
#
# - The original ordering does NOT need to be preserved.
# - Return the modified list.
#
# Example:
#
# numbers = [7, 3, 11, 4, 9, 2]
# pivot = 5
#
# A valid result:
#
# [2, 3, 4, 11, 9, 7]
#
# Another valid result:
#
# [4, 3, 2, 11, 9, 7]
#
# Both are correct because every value < 5 is on the
# left side and every value >= 5 is on the right side.
#
# Important:
#
# - Do not use sorted()
# - Do not use sort()
# - Do not create another list
# - Try to solve it with the control-flow/state tools
#   we've learned.
#
# ==========================================================


numbers = [7, 3, 11, 4, 9, 2]

def partition(numbers, pivot):

    left = 0
    right = len(numbers) -1

    while left < right:

        if numbers[left] < pivot:
            left += 1
            continue

        if numbers[right] >= 5:
            right -= 1
            continue

        elif numbers[left] > pivot and numbers[right] <= pivot:
            numbers[left], numbers[right] = numbers[right], numbers[left]
            left += 1
            right -= 1

    return numbers

print(partition(numbers, 5))

 # rejected solution by fatty patty
 # issue with skipping a del pos needs fixing
 # no cheating allowed
def partition_rejected(numbers, pivot):

    for pos, number in enumerate(numbers):
        if number >= 5:
            numbers.append(number)
            del numbers[pos]
        else:
            numbers.insert[0, number]
            del numbers[pos]

    return numbers

