# ==========================================================
# 04_linear_search.py
#
# Create a function:
#
# linear_search(students, target)
#
# Requirements:
#
# - Traverse the list.
# - If target is found, return the student's position.
# - If target isn't found, return None.
#
# Example:
#
# students = ["Alice", "Bob", "Charlie", "Diana"]
#
# linear_search(students, "Charlie")
# → 2
#
# linear_search(students, "Emma")
# → None
#
# Don't use .index()
# ==========================================================


students = [
    "Alice",
    "Bob",
    "Charlie",
    "Diana"
]


def linear_search(students, target):

    for position, student in enumerate(students):
        if student == target:
            return position

    return None

print(linear_search(students, "Charlie"))
print(linear_search(students, "Emma"))