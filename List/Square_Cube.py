# Create three lists of numbers, their squares and cubes

# Create a list of number
numbers = [1, 2, 3, 4, 5]
# Create lists to store squares and cubes
squares = []
cubes = []

# Calculate squares and cubes for each number
for num in numbers:
  squares.append(num * num)
  cubes.append(num * num * num)

# Print the original list, squares, and cubes
print("Numbers:", numbers)  # Output: Numbers: [1, 2, 3, 4, 5]
print("Squares:", squares)# Output: Squares: [1, 4, 9, 16, 25]
print("Cubes:", cubes)# Output: Cubes: [1, 8, 27, 64, 125]
