n = int(input())


cnt =0
arr =[]
for _ in range(n):
    arr.append(int(input()))

for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        cnt +=1

print(cnt)