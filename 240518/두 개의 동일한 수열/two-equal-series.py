n = int(input())

arrA = list(map(int,input().split()))
arrB = list(map(int,input().split()))

arrA.sort()
arrB.sort()

isTrue = "Yes"

for i in range(n):
    if arrA[i] != arrB[i]:
        isTrue ="No"
        break


print(isTrue)