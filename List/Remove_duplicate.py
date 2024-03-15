# Program to remove duplicate elements from the list

# Using set()

my_list = [1, 2, 2, 3, 4, 1, 5]
#  Using set() to create a new list without duplicates
unique_list1 = list(set(my_list))

print("Unique elements :", unique_list1) #Output: Unique elements : [1, 2, 3, 4, 5]
