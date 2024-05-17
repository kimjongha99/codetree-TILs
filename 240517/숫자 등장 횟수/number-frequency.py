n , m = map(int,input().split())

arr = list(map(int,input().split()))

x ,y = map(int,input().split())
di= {}

for elem in arr:
    if elem in di:
        di[elem]+=1
    else:
        di[elem]=1


if x in di:
    x1= (di[x])
else:
    x1 =0

if y in di:
    x2 = (di[y])
else:
    x2 =0


print(x1,x2)