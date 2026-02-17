def calculate_total(items):
    total = 0
    for item in items:
        print(f"Adding {item} to total.")
        total += item
    return total

if __name__ == "__main__":
    print("Total:", calculate_total([10, 20, 30]))