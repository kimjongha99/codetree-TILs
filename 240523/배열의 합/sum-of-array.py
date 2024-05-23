arr = [
    list(map(int,input().split()))
    for _ in range(4)
]



for row in arr:
    print(sum(row))