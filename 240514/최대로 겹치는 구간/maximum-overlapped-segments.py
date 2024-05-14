n = int(input())


arr = [0] * 100

for i in range(n):
    x,y = map(int,input().split())
    for j in range(x,y):
        arr[j]+= 1


print (max(arr))