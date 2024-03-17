# Program to replace all occurrences of string YOU with I without using extra space.
# Input: YOU AND PES
# Output: I AND PES


def replace_you_with_i(input_string):
    # Convert the input string to a list of characters for in-place modification
    characters = list(input_string)
    
    # Length of the string "YOU"
    you_length = len("YOU")
    
    # Iterate over the characters in the string
    for i in range(len(characters) - you_length + 1):
        # Check if the current substring matches "YOU"
        if ''.join(characters[i:i+you_length]) == "YOU":
            # Replace "YOU" with "I"
            characters[i:i+you_length] = "I"
    
    # Convert the list of characters back to a string
    replaced_string = ''.join(characters)
    
    return replaced_string

# Example usage:
input_string = "YOU AND PES"
result = replace_you_with_i(input_string)
print("Original string:", input_string)
print("Replaced string:", result)

