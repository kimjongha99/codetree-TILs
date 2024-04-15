str_2d=[
    list(input().split())
    for _ in range(5)
]



for row in str_2d:
    for elem in row:
        print(chr(ord(elem)-32),end=" ")
    print()