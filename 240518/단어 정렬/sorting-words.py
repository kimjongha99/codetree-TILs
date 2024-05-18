tc = int(input())


arr =[]

for _ in range(tc):
    str = input()
    arr.append(str)


sorted_arr =sorted(arr)

for ele in sorted_arr:
    print(ele)