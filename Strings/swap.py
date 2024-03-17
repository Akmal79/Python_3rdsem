# Write a function to accept a string & swap the adjacent characters and make a new string.

def swap_adjacent_characters(input_string):
    # Convert the input string to a list of characters for easy swapping
    characters = list(input_string)
    
    # Iterate over the characters two at a time and swap them
    for i in range(0, len(characters) - 1, 2):
        characters[i], characters[i + 1] = characters[i + 1], characters[i]
    
    # Convert the list of characters back to a string
    swapped_string = ''.join(characters)
    
    return swapped_string

# Example usage:
input_string = "abcdef"
result = swap_adjacent_characters(input_string)
print("Original string:", input_string)
print("Swapped string:", result)
