n = int(input())

arr = [
    list(map(int,input().split()))
    for _ in range(n)
]


max_count =0
for i in range(n):
    for j in range(n-2):
        max_count = max(max_count,arr[i][j] +arr[i][j+1]+arr[i][j+2])

print(max_count)