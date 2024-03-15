# Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# also create a lambda function that multiplies argument x with argument y and prints the result


# Lambda function to add 15 to a number
add_fifteen = lambda x: x + 15

# Call the lambda function with a value
result = add_fifteen(20)
print("Adding 15 to 20:", result)  # Output: Adding 15 to 20: 35

# Lambda function to multiply two arguments
multiply = lambda x, y: x * y

# Call the lambda function with values
product = multiply(5, 3)
print("Multiplying 5 and 3:", product)  # Output: Multiplying 5 and 3: 15
