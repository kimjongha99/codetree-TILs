n , k = map(int,input().split())

arr =list(map(int,input().split()))


di ={}

for i in range(n):
    if arr[i] in di:
        di[arr[i]] +=1
    else:
        di[arr[i]] =1


items = list(di.items())

items.sort(key=lambda x:x[0],reverse=True)
items.sort(key=lambda x:x[1],reverse=True)


for i in range(k):
    print(items[i][0], end=' ')