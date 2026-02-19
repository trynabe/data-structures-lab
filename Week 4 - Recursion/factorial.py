# Factorial (Recursive Code)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Recursive Result : {factorial(5)}")

# Factorial (Iterative Code)
n = 5
def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
print(f"Iterative Result : {fact_iter(n)}")