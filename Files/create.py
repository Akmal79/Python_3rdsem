# Create a file called input.txt with the contents “Keep apple and orange in
# the basket”. Read the file input.txt.
# Create a new file named vowels.txt, which contain only those words which
# start with a lowercase vowel (i.e. with &#39;a&#39;, &#39;e&#39;, &#39;i&#39;, &#39;o&#39;, ‘u’)
# Output : The vowel.txt shall contain “apple and orange in”

with open("input.txt", "w") as f:
    f.write("Keep apple and orange in the basket")

with open("input.txt", "r") as f:
    text = f.read()

with open("vowels.txt", "w") as f:
    for word in text.split():
        if word[0].lower() in "aeiou":
            f.write(word + " ")