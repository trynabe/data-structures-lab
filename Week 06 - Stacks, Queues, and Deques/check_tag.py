from array_stack import ArrayStack

def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; False otherwise."""
    S = ArrayStack()
    j = raw.find('<') # Find the first '<' character
    while j != -1:
        k = raw.find('>', j + 1) # Find the next '>' character
        if k == -1:
            return False # Invalid tag if '>' not found
        tag = raw[j + 1:k] # Extract the tag
        if not tag.startswith('/'): # Opening tag
            S.push(tag)
        else: # Closing tag
            if S.is_empty():
                return False # No matching opening tag
            if tag[1:] != S.pop(): # Match closing tag with the last opening tag
                return False
        j = raw.find('<', k + 1) # Find the next '<' character
    return S.is_empty() # Check if all tags were matched