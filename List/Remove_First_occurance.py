#  Program to remove first occurrence of a given element in the list

# We define a list my_list and the element to remove (element_to_remove).
# We use list comprehension to create a new list (new_list). 
# The comprehension iterates through the original list (my_list) and includes only elements (x) that are not equal to the element_to_remove.
# This approach avoids modifying the original list directly.
# Optionally, you can assign the new_list back to the original variable my_list to update it in-place.
# Finally, we print the modified list, which no longer contains the first occurrence of the removed element.

my_list = [3, 1, 4, 1, 5]
element_to_remove = 1

# Use list comprehension to create a new list without the first occurrence
new_list = [x for x in my_list if x != element_to_remove]

# Optional: Assign the new list back to the original variable
my_list = new_list

print(my_list)  # Output: [3, 4, 1, 5]
