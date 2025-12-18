def swap (x, y):
    # Check if x and y are numeric (i.e. int or float) 
    if not isinstance(x, (int, float)):
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
