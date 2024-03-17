# Count the number of times the word - python
# is repeated in a file called
# python_programming.txt.

with open("python_programming.txt", "r") as file1:
    contents = file1.read()
    count_python = contents.count("python")
print("python is repeated", count_python, "times")