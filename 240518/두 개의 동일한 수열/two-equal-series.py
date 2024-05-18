n = int(input())

arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

arrA.sort()
arrB.sort()

isTrue = "No"

for i in range(n):
    if arrA[i]== arrB[i]:
        isTrue ="Yes"
    else:
        isTrue = "No"


print(isTrue)