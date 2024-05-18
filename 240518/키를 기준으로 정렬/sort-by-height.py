n = int(input())

arr = []

for _ in range(n):
    secret_code, key, body = input().split()
    arr2 = [secret_code,key,body]
    arr.append(arr2)

sort_arr = sorted(arr,key=lambda x:x[1],reverse=False)


for name,height ,weight in sort_arr:
    print(name,height,weight)