from time import time  # Import time module

def compute_average(n):
    """Perform n appends to an empty list and return average time elapsed."""
    data = []
    start = time()  # Record the start time
    for k in range(n):
        data.append(None)  # Perform append
    end = time()  # Record the end time
    return (end - start) / n  # Compute average time per operation