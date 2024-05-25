n = int(input())

arr = list(map(int,input().split()))

ans =[]

for ele in arr:
    if ele%2==0:
        ans.append(ele)



for ele in ans[::-1]:
    print(ele, end=" ")