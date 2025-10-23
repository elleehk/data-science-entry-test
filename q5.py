def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    return

Answer:

def check_divisibility(num, divisor):
    
    # Check if num and divisor are numeric
    if not (type(num).__name__ in ('int', 'float') and type(divisor).__name__ in ('int', 'float')):
        return False
    
    # Check for division by zero
    if divisor == 0:
        return False

    # Check divisibility
    return num % divisor == 0

# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3

Answer:

print(check_divisibility(10, 2))

print(check_divisibility(7, 3))


