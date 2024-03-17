# Program to delete the characters from string1 which are present in string2 and print the new
# string.
# input: string1: whatsapp
# string2: wat
# output: hspp
def delete_chars(string1, string2):

  new_string = ""
  for char in string1:
    if char not in string2:
      new_string += char
  return new_string

string1 = "whatsapp"
string2 = "wat"

result = delete_chars(string1, string2)
print(result)  # Output: hspp
