# Print the count of words which starts with the letter ‘p’ from
# the file python_programming.txt. This count must be written to a
# new file p_count.txt.

with open("python_programming.txt", "r") as f:
    text = f.read()

words_starting_with_p = [word for word in text.split() if word[0] == 'p']

with open("p_count.txt", "w") as f:
    f.write(str(len(words_starting_with_p)))

