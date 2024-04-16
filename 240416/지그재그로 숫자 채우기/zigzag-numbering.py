n , m = map(int,input().split())

arr_2d=[
    [0 for _ in range(m)]
    for _ in range(n)
]


num =0
for col in range(m):
    if col % 2 ==0:
        for row in range(n):
            arr_2d[row][col]= num
            num+=1
    else:
        for row in range(n-1,-1,-1):
            arr_2d[row][col] =num
            num+=1

for row in range(n):
    for col in range(m):
        print(arr_2d[row][col], end = ' ')
    print()