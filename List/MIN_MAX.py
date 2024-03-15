# Program to find the position of minimum and maximum elements of a list 

# The code first defines a list my_list containing some numbers.
# Then, it uses the built-in min() function to find the minimum element in the list.
# The index() method is used to find the index of the minimum element within the list.
# Similarly, the max() function is used to find the maximum element, and its index is found using the index() method.
# Finally, the code prints the indexes of the minimum and maximum elements.

my_list = [8, 2, 1, 9, 5, 6]

# Find the index of the minimum element
min_index = my_list.index(min(my_list))

# Find the index of the maximum element
max_index = my_list.index(max(my_list))
print("Index of minimum element:", min_index)  # Output: Index of minimum element: 2
print("Index of maximum element:", max_index)  # Output: Index of maximum element: 3
