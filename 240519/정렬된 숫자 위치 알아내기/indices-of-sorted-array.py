n = int(input())

arr = list(map(int,input().split()))

origin_arr = []

for i in range(n):
    origin_arr.append([arr[i],i])


sorted_arr = sorted(origin_arr)

ans = [0]*n


for i in range(n):
    val, original_index = sorted_arr[i]
    ans[original_index] = i+1


# 결과 출력
for position in ans:
    print(position, end=" ")