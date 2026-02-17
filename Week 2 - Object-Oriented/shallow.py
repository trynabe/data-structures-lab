import copy

# Original nested list
original = [[1, 2, 3], [4, 5, 6]]

# Create an alias (reference to the same object)
alias = original

# Shallow copy
shallow_copy = copy.copy(original)

# Deep copy
deep_copy = copy.deepcopy(original)

# Modify the original list
original[0][0] = 99

# Print all lists to observe behavior
print("Original:", original)
print("Alias (Reference):", alias)
print("Shallow Copy:", shallow_copy)
print("Deep Copy:", deep_copy)