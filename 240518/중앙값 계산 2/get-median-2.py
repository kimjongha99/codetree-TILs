n = int(input())

arr = list(map(int,input().split()))

ans =[]


for i in range(0,n,2):
    sub_arr = arr[0:i+1]
    sub_arr.sort()

    ans.append(sub_arr[len(sub_arr)//2])


for ele in ans:
    print(ele, end=" ")