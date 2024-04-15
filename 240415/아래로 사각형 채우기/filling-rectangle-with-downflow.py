n = int(input())

# Initialize a 2D array with zeros of size n x n
arr_2d = [[0 for _ in range(n)] for _ in range(n)]

# We'll start numbering from 1
num = 1

# Fill the array by columns
for j in range(n):  # iterating over columns
    for i in range(n):  # iterating over rows
        arr_2d[i][j] = num
        num += 1

# Print the array
for row in arr_2d:
    for elem in row:
        print(elem, end=" ")
    print()