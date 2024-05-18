n, k , str = input().split()
n = int(n)
k = int(k)

arr =[]
for _ in range(n):
    c = input()
    if c.startswith(str,0,len(str)):
        arr.append(c)


arr_sort = sorted(arr,key=lambda x:x, reverse=False)

print(arr_sort[k-1])