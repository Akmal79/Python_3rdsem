# Python code to demonstrate working of
# Cartesian product of string elements
# Using split() + list comprehension

# Initializing strings
str1 = "abc"
str2 = "ab"

product = []
for char1 in str1:
  for char2 in str2:
    product.append(f"{char1},{char2}")

print(*product, sep="\n")

