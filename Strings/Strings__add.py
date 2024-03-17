#   Combines characters from two strings, alternating their order.

#   Args:
#       str1: The first string.
#       str2: The second string.

#   Returns:
#       The combined string with characters from both strings in alternating order.

def combine_strings(str1, str2):

  result = ""
  i, j = 0, 0
  while i < len(str1) and j < len(str2):
    result += str1[i] + str2[j]
    i += 1
    j += 1

  # Append remaining characters from the longer string (if any)
  result += str1[i:] + str2[j:]

  return result

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

combined_string = combine_strings(str1, str2)
print(combined_string)



