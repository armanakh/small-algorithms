# ==========================================================
# 05_filter_elements.py
#
# Create:
#
# filter_students(students, letter)
#
# Requirements:
#
# - Traverse the list.
# - Keep every student whose name starts with `letter`.
# - Return a NEW list.
# - Do not modify the original list.
#
# Example:
#
# students = ["Alice", "Bob", "Andrew", "Diana"]
#
# filter_students(students, "A")
# → ["Alice", "Andrew"]
#
# filter_students(students, "B")
# → ["Bob"]
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Andrew",
    "Diana"
]


def filter_students(students, letter):
    filtered_students = []

    for student in students:
        if student[0] == letter:
            filtered_students.append(student)

    return filtered_students

filter = filter_students(students, "A")

print(filter)
