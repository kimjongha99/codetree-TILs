n = int(input())


data =[]


for i in range(1, n + 1):
    line = list(map(int, input().split()))
    new_val = line + [i]
    data.append(new_val)

data.sort(key=lambda x: (x[0], -x[1]))


for row in data:
    for ele in row:
        print(ele , end =" ")
    print()