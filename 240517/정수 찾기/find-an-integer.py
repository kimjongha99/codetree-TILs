n1 = int(input())

arr1 = list(map(int,input().split()))


n2 = int(input())

arr2 = list(map(int,input().split()))


s1 = set(arr2)


for elem in s1:
    if elem in arr1:
        print(1)
    else:
        print(0)