n1 = int(input())

arr1 = list(map(int,input().split()))


n2 = int(input())

arr2 = list(map(int,input().split()))


s1= set(arr1)

result = []

for num in arr2:
    if num in s1:
        result.append(1)
    else:
        result.append(0)


for elem in result:
    print(elem, end= " ")