n = int(input())

arr = list(map(int,input().split()))


desc_arr = sorted(arr, key= lambda x:x , reverse= True)

for elem in desc_arr:
    print(elem, end=" ")


print()
asc_arr = sorted(arr, key= lambda x:x , reverse= False)

for elem in asc_arr:
    print(elem, end=" ")