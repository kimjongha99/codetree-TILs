n = int(input())

# Initialize an array to track the number of times each position is passed
# We use 2001 to cover the range from -1000 to 1000
arr = [0] * 2001

# The starting point, which represents position 0
point = 1000

# Define functions to move left and right
def move_right(x):
    global point
    for j in range(point, point + x):
        arr[j] += 1
    point += x

def move_left(x):
    global point
    for j in range(point - 1, point - x - 1, -1):
        arr[j] += 1
    point -= x

# Read the commands and execute the moves
for _ in range(n):
    x_str, direction = input().split()
    x = int(x_str)
    if direction == 'R':
        move_right(x)
    elif direction == 'L':
        move_left(x)

# Count the number of positions passed more than twice
count = 0
for elem in arr:
    if elem >= 2:  # We want positions passed more than twice
        count += 1

print(count)