import sys

# Initialize an empty list
data = []

# Print the header
print(f"{'Length':<10}{'Size in Bytes':<15}")
print("-" * 25)

# Append elements to the list and track size
for k in range(50):  # Experiment with appending 50 elements
    length = len(data)
    size_in_bytes = sys.getsizeof(data)
    print(f"{length:<10}{size_in_bytes:<15}")
    data.append(None)  # Add an element to the list