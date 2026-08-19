# ==========================================================
# 07_count_occurrences.py
#
# Create:
#
# count_student(students, target)
#
# Requirements:
#
# - Traverse the list.
# - Count how many times target appears.
# - Return the count.
# - Do not use .count()
#
# Example:
#
# ["Alice", "Bob", "Bob", "Diana"]
# target = "Bob"
# → 2
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Bob",
    "Charlie",
    "Diana",
    "Bob"
]


def count_student(students, target):
    count = 0
    for student in students:
        if student == target:
            count += 1
    return count

print(count_student(students, "Bob"))
