
# Challenge What is the runtime complexity of this function

def power_r(a, b):
    # Error checking
    # try to cast our exponent to an int
    try:
        _ = int(b) # O(1)
    # exception on fail with error message
    except ValueError:
        print("Exponent (b) must be and integer") # O(1)
        # and return
        return # O(1)

    # base case
    # anything raised to the power of 0 will be one
    if b == 0:
        return 1 # O(1)
    # positive case if b is greater than zero
    elif b > 0:   
        # Recursive case
        # Call the function on b - 1
        return a * power_r(a, b - 1) # O(n)
    # Recursive negative exponent
    else:
        # return 1 divided by a multiplied by the function with -b - 1
        return 1 / (a * power_r(a, -b - 1)) # O(1)
        # or return 1 divided by function with -b
        # return 1 / power_r(a, -b)

# O(n)
