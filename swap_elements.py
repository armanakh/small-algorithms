# ==========================================================
# 11_swap_elements.py
#
# Create:
#
# swap_students(students, first, second)
#
# Requirements:
#
# - Swap the elements at positions `first` and `second`.
# - Modify the original list.
# - Return the modified list.
#
# Example:
#
# ["Alice", "Bob", "Charlie", "Diana"]
#
# first = 0
# second = 3
#
# → ["Diana", "Bob", "Charlie", "Alice"]
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana"
]


def swap_students(students, first, second):
    keep_student = students[first]
    students[first] = students[second]
    students[second] = keep_student

    return students

print(swap_students(students, 0, 3))
