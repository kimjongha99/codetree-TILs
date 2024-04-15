n=4

arr_2d = [
  list(map( int,input().split()))
    for _ in range(n)
]


num=0

for row in arr_2d:
    for i, elem in enumerate(row):
        num+=elem
        if i%4==3:
            print(num)
            num=0