# ==========================================================
# 08_replace_element.py
#
# Create:
#
# replace_student(students, target, replacement)
#
# Requirements:
#
# - Traverse the list.
# - Find the FIRST occurrence of target.
# - Replace it with replacement.
# - Return the modified list.
# - If target isn't found, return None.
#
# Example:
#
# ["Alice", "Bob", "Diana"]
# target = "Bob"
# replacement = "Charlie"
#
# → ["Alice", "Charlie", "Diana"]
#
# Only replace the FIRST match.
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "Bob",
    "Diana"
]


def replace_student(students, target, replacement):
    for pos, student in enumerate(students):
        if student == target:
            students[pos] = replacement

            return students
    return None

print(replace_student(students, "Bob", "Charlize"))

