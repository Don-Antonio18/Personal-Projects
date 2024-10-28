def encoded_string(lst):
    if lst == "":  # Base case: if the string is empty, return an empty string
        return ""
    else:
        first_char = ord(lst[0])  # Get the ASCII value of the first character
        # Check if the ASCII value is even
        if first_char % 2 == 0:
            first_char += 4
        else:
            first_char += 2
        # Convert back to character and concatenate with the recursive call on the rest of the string
        return chr(first_char) + encoded_string(lst[1:])

# Test the function
print(encoded_string("hello"))  # Expected output: 'lgppq'
