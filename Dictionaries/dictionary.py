# Create a sample dictionary
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York",
    "skills": ["Python", "Java"]
}

# Accessing Values
print("Name:", person["name"])  # Using key to access value

# Checking Key Existence (Avoids KeyError)
if "country" in person:
    print(f"Country: {person['country']}")  # Access only if key exists (assuming 'country' is not present)
else:
    print("Country key not found")

# Adding New Key-Value Pair
person["occupation"] = "Software Engineer"
print(person)

# Modifying an Existing Value
person["age"] = 31
print(person)

# Removing a Key-Value Pair
del person["skills"]
print(person)

# Iterating Over Keys
for key in person:
    print(f"{key}: {person[key]}")

# Iterating Over Key-Value Pairs (using items())
for key, value in person.items():
    print(f"{key}: {value}")

# Getting All Keys (using keys())
all_keys = person.keys()
print("All Keys:", all_keys)

# Getting All Values (using values())
all_values = person.values()
print("All Values:", all_values)

# Copying a Dictionary (using copy())
person_copy = person.copy()
person_copy["city"] = "Los Angeles"  # Modify the copy without affecting the original
print("Original Person:", person)
print("Copied Person:", person_copy)

# Clearing a Dictionary (using clear())
person.clear()
print(person)  # Now an empty dictionary


