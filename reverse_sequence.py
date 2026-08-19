# ==========================================================
# 12_reverse_sequence.py
#
# Create:
#
# reverse_students(students)
#
# Requirements:
#
# - Reverse the list IN PLACE.
# - Do not create a second list.
# - Return the modified list.
#
# Example:
#
# ["Alice", "Bob", "Charlie", "Diana"]
#
# → ["Diana", "Charlie", "Bob", "Alice"]
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana",
    "Momo"
]


def reverse_students(students):
    
    pos = 0
    reverse = len(students) - 1
    while pos < len(students) // 2:
        keep_student = students[reverse]
        students[reverse] = students[pos]
        students[pos] = keep_student
        pos += 1
        reverse -= 1

    return students

print(reverse_students(students))
