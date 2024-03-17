# Create some sets
fruits = {"apple", "banana", "orange"}
vegetables = {"carrot", "pea", "lettuce", "cucumber"}

# Union - elements in either set (or both)
fruit_and_veg = fruits | vegetables  # or fruits.union(vegetables)
print("Union:", fruit_and_veg) # output: Union: {'apple', 'carrot', 'cucumber', 'lettuce', 'pea', 'banana', 'orange'}

# Intersection - elements common to both sets
overlap = fruits & vegetables  # or fruits.intersection(vegetables)
print("Intersection:", overlap) # output: Intersection: set()

# Difference - elements in fruits but not vegetables
fruit_diff = fruits - vegetables  # or fruits.difference(vegetables)
print("Difference (fruits not in vegetables):", fruit_diff)#output: Difference (fruits not in vegetables): {'apple', 'banana', 'orange'}

# Symmetric Difference - elements in one set but not the other (not in both)
diff_both = fruits ^ vegetables  # or fruits.symmetric_difference(vegetables)
print("Symmetric Difference:", diff_both) #Output: Symmetric Difference: {'cucumber', 'lettuce', 'pea', 'orange', 'carrot', 'apple', 'banana'}