# Program to find the differences of two lists 

# Using List comprehension
# We define two lists list1 and list2 (with duplicates).
# We use list comprehension to create new lists.
# The first comprehension (difference1) iterates through list1 and includes elements (x) that are not found in list2 using the not in operator.
# The second comprehension (difference2) does the same for list2.
# We print both differences as lists, which preserve duplicates if they exist in the original lists.


list1 = [1, 2, 3, 2, 1]
list2 = [3, 4, 5, 2, 1]
# Find elements in list1 not in list2 using list comprehension
difference1 = [x for x in list1 if x not in list2]

# Find elements in list2 not in list1 using list comprehension
difference2 = [x for x in list2 if x not in list1]

# Print the differences (as lists)
print("Difference 1 (elements in list1 but not list2):", difference1)
print("Difference 2 (elements in list2 but not list1):", difference2)

# Output Difference 1 (elements in list1 but not list2): []
# Difference 2 (elements in list2 but not list1): [4, 5]
