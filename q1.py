def swap (x, y):
    # Check if x and y are numeric (i.e. int or float) by testing its type after adding 0
    try:
        x + 0
        y + 0
        if not (type(x).__name__ in ('int', 'float') and type(y).__name__ in ('int', 'float')):
            return -1
    except TypeError:
        return -1
    # Swap the values using arithmetic manipulation
    x = x + y
    y = x - y
    x = x - y
    # Display numerals after swapping
    print("x =", x, ", y =", y) 

# Task 2
# Invoke the function "swap" using the following scenarios:
# - "Apple", 10
# - 9, 17

swap ("Apple", 10)
swap (9, 17)
