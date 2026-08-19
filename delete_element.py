# ==========================================================
# 09_delete_element.py
#
# Create:
#
# delete_student(students, target)
#
# Requirements:
#
# - Traverse the list.
# - Find the FIRST occurrence of target.
# - Delete it.
# - Stop immediately after deleting it.
# - If target isn't found, return None.
#
# Example:
#
# ["Alice", "Bob", "Charlie", "Bob", "Diana"]
#
# target = "Bob"
#
# → ["Alice", "Charlie", "Bob", "Diana"]
#
# Only delete the FIRST match.
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "Bob",
    "Diana"
]


def delete_student(students, target):
    for pos, student in enumerate(students):
        if student == target:
            del students[pos]

            return students
    return None

print(delete_student(students, "Bob"))


