# Assuming the previously defined skip_power function
def skip_power(n, k):
    if n < k:
        return 0  # Base case: if n is less than k, return 0
    else:
        return n ** k + skip_power(n - k, k)  # Return n raised to k plus the result of the recursive call

from lab3Q3 import sumDigits  # Importing sumDigits function

def skip_valid_power(a, b):
    # Get the result from skip_power
    result = skip_power(a, b)
    
    # Check if result is within the range and validate sum of digits
    if 1000 <= result <= 999999 and sumDigits(result) % 7 == 0:
        return True
    return False

# Example usage
print(skip_valid_power(10, 4))  # Expected output: True
print(skip_valid_power(12, 6))  # Expected output: False