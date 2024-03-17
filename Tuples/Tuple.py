# Create a sample tuple
fruits = ("apple", "banana", "orange", "mango")

# Accessing Elements
print("First fruit:", fruits[0])  # Accessing by index
print("Last fruit:", fruits[-1])  # Accessing the last element

# Slicing (extracting sub-tuples)
citrus_fruits = fruits[1:3]  # Extracts "banana" and "orange" (from index 1 to 2, excluding element at index 2)
print("Citrus fruits:", citrus_fruits)

# Immutability (attempting modification results in an error)
# fruits[0] = "kiwi"  # This will cause a TypeError

# Tuple Concatenation (combining tuples)
all_fruits = fruits + citrus_fruits
print("All fruits:", all_fruits)

# Length of a tuple
fruit_count = len(fruits)
print("Number of fruits:", fruit_count)

# Checking for Element Existence (using the 'in' operator)
if "mango" in fruits:
    print("Mango is present")

# Looping through elements
for fruit in fruits:
    print(fruit)

# Membership Testing (using the 'in' operator with other data types)
if "apple" not in citrus_fruits:
    print("Apple is not a citrus fruit")

# Minimum and Maximum Values (using min() and max() for comparable data types)
print("Minimum fruit:", min(fruits))  # Alphabetically first item
print("Maximum fruit:", max(fruits))  # Alphabetically last item

# Counting Element Occurrences (using the 'count()' method)
banana_count = fruits.count("banana")
print("Number of bananas:", banana_count)
