n = int(input())


arr = [0] * 201

for i in range(n):
    x,y = map(int,input().split())
    for j in range(x + 100, y + 100):
        arr[j] += 1

print (max(arr))