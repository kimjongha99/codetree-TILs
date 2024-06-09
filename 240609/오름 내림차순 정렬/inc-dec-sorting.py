n = int(input())

arr = list(map(int,input().split()))

new_arr1 = sorted(arr)
print(" ".join(map(str, new_arr1)))

new_arr2 = sorted(arr,key = lambda x : x, reverse =True )

print(" ".join(map(str, new_arr2)))