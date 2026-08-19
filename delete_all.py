# ==========================================================
# 10_delete_all.py
#
# Create:
#
# delete_all(students, target)
#
# Requirements:
#
# - Delete EVERY occurrence of target.
# - Modify the original list.
# - Return the modified list.
#
# Example:
#
# ["Alice", "Bob", "Charlie", "Bob", "Diana", "Bob"]
#
# target = "Bob"
#
# → ["Alice", "Charlie", "Diana"]
#
# You may NOT create a second list.
#
# ==========================================================

students = [
    "Alice",
    "Bob",
    "Charlie",
    "james",
    "Bob",
    "Diana",
    "Bob"
]


def delete_all(students, target):
    pos = 0

    while pos < len(students):

        if students[pos] == target:
            del students[pos]

        else:
            pos += 1
            
    return students

print(delete_all(students, "Bob"))
