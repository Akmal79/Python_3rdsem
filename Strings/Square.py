text = input("Enter a string: ")

squares = []  # Create an empty list to store squares

for char in text:
  if char.isdigit():  # Check if character is a digit
    number = int(char)
    squares.append(number * number)  # Calculate and add square to list

if squares:  # If any squares were found
  print(*squares)  # Print squares with spaces in between
else:
  print("No numbers found in the string.")
