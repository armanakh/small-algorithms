# Longest increasing streak

numbers = [2, 4, 7, 8, 9, 10, 3, 5, 6, 8, 5]

streak = 1
longest_streak = 1

for pos, element in enumerate(numbers[1:], start=1):

    previous = numbers[pos - 1]

    if previous < element:
        streak += 1
    else:
        streak = 1

    if streak > longest_streak:
        longest_streak = streak

print(longest_streak)