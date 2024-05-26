n = int(input())


arr = list(map(int,input().split()))


idx=0


for  i, ele in enumerate(arr):
    if ele ==2:
        idx+=1
        if idx ==3:
            print(i+1)