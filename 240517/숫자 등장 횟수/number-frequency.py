n, m = tuple(map(int, input().split()))

arr = list(map(int,input().split()))

x ,y = map(int,input().split())
di= {}

for elem in arr:
    if elem in di:
        di[elem]+=1
    else:
        di[elem]=1


# if x in di:
#     x1= (di[x])
# else:
#     x1 =0
#
# if y in di:
#     x2 = (di[y])
# else:
#     x2 =0
# Get the count for x and y, default to 0 if not found
x1 = di.get(x, 0)
x2 = di.get(y, 0)


print(x1,x2)