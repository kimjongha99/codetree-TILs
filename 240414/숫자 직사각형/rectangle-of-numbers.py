n = int(input())
m = int(input())

arr_2d=[]
current_num = 1
for i in range(n):
    row =[]
    for j in range(m):
        row.append(current_num)
        current_num+=1
    arr_2d.append(row)


for row in arr_2d:
    print(" ".join(map(str,row )))