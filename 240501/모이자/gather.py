n  = int(input())

arr = list(map(int,input().split()))

ans_list = []


for i in range(n):
    total_distance  =0
    for j in range(n):
        total_distance  += abs(j-i) * arr[j]
    ans_list.append(total_distance)

print(min(ans_list))