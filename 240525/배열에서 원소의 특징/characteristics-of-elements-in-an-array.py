arr = list(map(int,input().split()))

for i, ele in  enumerate(arr):
    if ele %3 ==0:
        print(arr[i-1])
        break