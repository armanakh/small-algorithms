# ==========================================================
# 06_transform_elements.py
#
# Create:
#
# transform_len(students)
#
# Requirements:
#
# - Traverse the list.
# - Replace every student name with its length.
# - Modify the original list.
# - Return the modified list.
#
# Example:
#
# ["Alice", "Bob", "Diana"]
# → [5, 3, 5]
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana"
]


def transform_len(students):
    for index, student in enumerate(students):
        students[index] = len(student)

    return students


transform_len(students)

print(students)
