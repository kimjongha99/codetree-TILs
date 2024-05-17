n1 = int(input())

arr1 = list(map(int,input().split()))


n2 = int(input())

arr2 = list(map(int,input().split()))



for elem in arr2:
    if elem in arr1:
        print(1)
    else:
        print(0)