#  Program to sort the elements of given list in Ascending and Descending Order

# Sorting a List of Tuples by a Specific Element
people = [("Alice", 30), ("Bob", 25), ("Charlie", 22)]
# Sort by age (second element in each tuple)
people.sort(key=lambda x: x[1])
print(people)  # Output: [('Charlie', 22), ('Bob', 25), ('Alice', 30)]
