# Find the number of characters and words in a file data.txt. Write this
# count to a new file.

with open("data.txt", "r") as f:
    text = f.read()

with open("count.txt", "w") as f:
    f.write("Characters: {}\n".format(len(text)))
    f.write("Words: {}\n".format(len(text.split())))