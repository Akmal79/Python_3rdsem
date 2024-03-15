# Program to Create two lists with EVEN numbers and ODD numbers from a list

# Create a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Create empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Separate even and odd numbers using list comprehension
even_numbers = [num for num in numbers if num % 2 == 0]
odd_numbers = [num for num in numbers if num % 2 != 0]

# Print the even and odd number lists
print("Even numbers:", even_numbers) #Output:Even numbers: [2, 4, 6, 8, 10]
print("Odd numbers:", odd_numbers) #Output:Odd numbers: [1, 3, 5, 7, 9]

