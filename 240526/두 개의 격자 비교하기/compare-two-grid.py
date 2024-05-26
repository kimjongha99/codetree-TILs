n , m = map(int,input().split())

arr1 =[
    list(map(int,input().split()))

    for _ in range(m)

]

arr2 = [
    list(map(int, input().split()))

    for _ in range(m)

]

check_arr =[
    [0 for _ in range(m)]

    for _ in range(n)
]



for i in range(n):
    for j in range(m):
        if arr1[i][j]==arr2[i][j]:
            check_arr[i][j]=0
        else:
            check_arr[i][j]=1


for row in check_arr:
    for ele in row:
        print(ele , end=" ")
    print()