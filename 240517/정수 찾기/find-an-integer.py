n1 = int(input())

arr1 = list(map(int,input().split()))


n2 = int(input())

arr2 = list(map(int,input().split()))

set1 = set(arr1)

result = []

for elem in arr2:
    if elem in set1:
        result.append(1)
    else:
        result.append(0)

print("\n".join(map(str, result)))