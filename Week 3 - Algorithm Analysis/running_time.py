# Type Loops - O(n)
n = 10
for i in range(0, n):
    print(i)

# Type Nested Loop - O(n**2)
for i in range(0, n):
    for j in range(0, n):
        print(i, j)

# Type Consecutive Statements - O(n**2)
n = 100
for i in range(0, n):
    print(i)
for i in range(0, n):
    for j in range(0, n):
        print(i, j)
    
# If Then Else - O(n)
if n == 1:
    print(n)
else:
    for i in range(0, n):
        print(i)