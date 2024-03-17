# Program to find if two strings are anagrams.
# Anagrams: Same set of letters with different arrangements. Number of times a letter
# present in one string must be equal to the number of times the letter is present on another
# string. Examples: elegant man , a gentleman

def are_anagrams(str1, str2):

  # Convert strings to lowercase and remove whitespaces
  str1 = str1.lower().replace(" ", "")
  str2 = str2.lower().replace(" ", "")

  # Check if string lengths are equal (anagrams must have the same length)
  if len(str1) != len(str2):
    return False

  # Create a character count dictionary for str1
  char_count = {}
  for char in str1:
    char_count[char] = char_count.get(char, 0) + 1

  # Check if all characters in str2 can be formed from str1's character counts
  for char in str2:
    if char not in char_count or char_count[char] == 0:
      return False
    char_count[char] -= 1

  return True

# Example usage
str1 = "silent"
str2 = "listen"

if are_anagrams(str1, str2):
  print(f"{str1} and {str2} are anagrams.")
else:
  print(f"{str1} and {str2} are not anagrams.")
