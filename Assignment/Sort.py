# 3.write a python program to get a list sorted by in increasing order
#  from the last element in each tuple from a given list of non empty tuple

def sort_tuples_by_last_element(tuples_list):
    # Use a lambda function as the key for sorting based on the last element
    sorted_list = sorted(tuples_list, key=lambda x: x[-1])
    return sorted_list

# Example usage:
my_tuples = [(1, 5, 3), (4, 2, 8), (7, 1, 6), (3, 9, 2)]
sorted_tuples = sort_tuples_by_last_element(my_tuples)
print("Sorted Tuples:", sorted_tuples) #Output: Sorted Tuples: [(3, 9, 2), (1, 5, 3), (7, 1, 6), (4, 2, 8)]
