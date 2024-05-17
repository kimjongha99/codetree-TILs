tc = int(input())

arr = []

for i in range(tc):
    x,y = map(int,input().split())
    arr.append((x,y))



arr.sort(key=lambda x:x[0],reverse=True)
arr.sort(key=lambda x:x[1],reverse=True)


di ={}

for item in arr:
    key = item[0]
    val = item[1]

    if key in di:
        di[key] = val
    else:
        di[key] =val


sum_val=0
for key in di:
    sum_val += di[key]

print(sum_val)