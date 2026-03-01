# reverse_file_tester.py

from array_stack import ArrayStack

def reverse_file(filename):
    """Reverse the contents of a file line-by-line."""
    S = ArrayStack()
    # Open the original file and push each line onto the stack
    with open(filename, 'r') as original:
        for line in original:
            S.push(line.strip('\n')) # strip newlines for cleaner output

    # Open the same file for writing and write the lines in reverse order
    with open(filename, 'w') as output:
        while not S.is_empty():
            output.write(S.pop() + '\n') # re-insert newlines while writing

# Example usage
if __name__ == "__main__":
    filename = 'example.txt' # Replace with your file path
    reverse_file(filename)
    print(f"The file '{filename}' has been reversed line-by-line.")