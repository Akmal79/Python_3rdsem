# Program to remove duplicate elements from the list

# Using dictionary
my_list = [1, 2, 2, 3, 4, 1, 5]

#  Using dictionary (more efficient for larger lists)
unique_list2 = []
seen = {}
for element in my_list:
  if element not in seen:
    unique_list2.append(element)
    seen[element] = True

print("Unique elements (Method 2):", unique_list2)
