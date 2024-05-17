n, k = map(int,input().split())

arr = list(map(int,input().split()))

di= {}
ans =0

for num in arr:
    if k-num in di:
        ans += di[k-num]

    if num in di:
        di[num] +=1
    else:
        di[num]=1

print(ans)