n = int(input())

arr = [int(input())
       for _ in range(n)
       ]

for ele in arr:
    if ele % 2 != 0 and ele % 3 ==0:
        print(ele)