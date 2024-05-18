n = int(input())

arr = list(map(int,input().split()))


sort_arr = sorted(arr)

ans =[]

count=0
for  i , ele  in enumerate(arr):
    for j in range(len(sort_arr)):
        count+=1
        if sort_arr[j] == ele:
            if count in ans:
                ans.append(count+1)
                break
            ans.append(count)

            count=0
            break

for ele in ans:
    print(ele , end=" ")