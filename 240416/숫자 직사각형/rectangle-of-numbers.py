n, m = tuple(map(int, input().split()))

arr_2d=[
    list(0 for _ in range(m))
    for _ in range(n)
]


num=1
for i in range(4):
    for j in range(3):
        arr_2d[i][j]+=num
        num+=1
        print(arr_2d[i][j], end=" ")
    print()