arr = list(map(int,input()))


n1 = 0


for i , val in enumerate(reversed(arr)):
    n1 += val*(2**i)


n2 = n1 * 17


arr2= []

while True:
    if n2<2:
        arr2.append(n2)
        break

    arr2.append(n2 % 2)
    n2 = n2//2


for elem in arr2[::-1]:
    print(elem, end="")