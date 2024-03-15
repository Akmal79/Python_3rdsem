# Program to find the differences of two lists 

# Using **Sets**
# We define two lists list1 and list2.
# We convert both lists to sets using set(). Sets eliminate duplicates.
# The - operator between sets finds the difference between them.
# difference1 contains elements present in list1 but not in list2.
# difference2 contains elements present in list2 but not in list1.
# We print both differences as sets.

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

# Find the difference between sets (removes duplicates)
difference1 = set(list1) - set(list2)
difference2 = set(list2) - set(list1)

# Print the differences (as sets)
print("Difference 1 (elements in list1 but not list2):", difference1)
print("Difference 2 (elements in list2 but not list1):", difference2)
# Output: Difference 1 (elements in list1 but not list2): {1, 2}
#         Difference 2 (elements in list2 but not list1): {6, 7}
