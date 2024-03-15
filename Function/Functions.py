# Positional and keyword parameters
def greet(name, message="Hello"):
    print(f"{message}, {name}!")

greet("Alice")  # Output: Hello, Alice!
greet(message="Hi", name="Bob")  # Output: Hi, Bob!

# Default parameters
def calculate(x, y=10):
    return x + y

result = calculate(5)  # Uses default y (10) - Output: 15
result = calculate(5, 2)  # Overrides default y - Output: 7

# Variable number of arguments
def print_all(*args):
    for arg in args:
        print(arg)

print_all(1, 2, 3, "hello")

# Recursion (example: factorial)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

fact = factorial(5)  # Output: 120

# Callback (example: sorting with a custom key)
def sort_by_length(items):
    def get_length(item):
        return len(item)
    return sorted(items, key=get_length)

names = ["Alice", "Bob", "Charlie"]
sorted_names = sort_by_length(names)  # Output: ["Bob", "Alice", "Charlie"]

# Closure (example: counter function)
def create_counter():
    count = 0

    def increment():
        nonlocal count  # Use `nonlocal` to modify the enclosing variable
        count += 1
        return count

    return increment

counter1 = create_counter()
counter2 = create_counter()

print(counter1())  # Output: 1
print(counter1())  # Output: 2
print(counter2())  # Output: 1 (separate counter)
