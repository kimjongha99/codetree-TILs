n  = int(input())



arr= []

for i in range(1,n+1):
    sub =[]
    arr.append(sub)
    for j in range(1,n+1):
        sub.append(j*i)


for row in arr:
    ans = sorted(row,key= lambda x:x,reverse=True)
    for ele in ans:
        print(ele , end=" ")
    print()