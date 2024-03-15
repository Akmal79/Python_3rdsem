# Write a Python program to sort a list of dictionaries using Lambda.
# Original list of dictionaries :
# [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#  {'make': 'Samsung', 'model': 7, 'color': 'Blue'}

# Sample list of dictionaries


data = [
    {'make': 'Nokia', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'}
]

# Sort by the 'model' key in ascending order (default)
# Sort by the 'model' key in ascending order (default)
sorted_by_model = sorted(data, key=lambda x: int(x['model']))
print("Sorted by model (ascending):", sorted_by_model)

# Sort by the 'color' key in descending order
sorted_by_color_desc = sorted(data, key=lambda x: x['color'], reverse=True)
print("Sorted by color (descending):", sorted_by_color_desc)

# # Output:
# Sorted by model (ascending): [{'make': 'Mi Max', 'model': '2', 'color': 'Gold'},
#  {'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

# Sorted by color (descending): [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]