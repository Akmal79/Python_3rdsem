# 2.write a python program to get the largest number from a list
def find_largest_number(lst):
    if not lst:
        return None  # Return None for an empty list
    return max(lst)

# Example usage:
my_list = [4, 7, 2, 9, 1, 12, 5]
largest_number = find_largest_number(my_list)
print("The largest number is:", largest_number) #Output:The largest number is: 12
