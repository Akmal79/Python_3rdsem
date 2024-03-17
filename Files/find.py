# Find the length of the longest word in a text file along with the longest
# word.

with open("text.txt", "r") as f:
    text = f.read()

words = text.split()
longest_word = max(words, key=len)
longest_length = len(longest_word)

print("Longest word:", longest_word)
print("Length:", longest_length)