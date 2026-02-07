def add_numbers(a: int, b: int) -> int:
    return a + b

# This should show an error - passing string to int parameter
result = add_numbers("hello", 5)

# This should show an error - wrong type assignment
x: int = "not a number"