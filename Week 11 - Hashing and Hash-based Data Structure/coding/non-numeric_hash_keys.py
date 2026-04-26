def custom_hash_key(string_key):
    """
    Method 1: Custom Transformation Function (A=1, B=2, C=3, ..., Z=26)
    """
    hash_value = 0
    print(f"--- Method 1: Custom mapping for '{string_key}' ---")
    for char in string_key.upper():
        if char.isalpha():
            val = ord(char) - 64
            hash_value += val
            print(f"Character {char} -> Value is {val}")
            
    return hash_value

def ascii_hash_key(string_key):
    """
    Method 2: Using standard ASCII character codes
    """
    hash_value = 0
    print(f"\n--- Method 2: ASCII mapping for '{string_key}' ---")
    for char in string_key:
        val = ord(char)
        hash_value += val
        print(f"Character {char} -> ASCII value is {val}")
        
    return hash_value

# ==========================================
# Testing with the word "CAT" from the slide
# ==========================================
word = "CAT"

# Test Method 1
result_custom = custom_hash_key(word)
print(f"Total Hash Value (Method 1) = {result_custom}")

# Test Method 2
result_ascii = ascii_hash_key(word)
print(f"Total Hash Value (Method 2) = {result_ascii}")