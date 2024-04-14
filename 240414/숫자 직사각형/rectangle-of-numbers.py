n = int(input("행의 개수(n)를 입력하세요: "))
m = int(input("열의 개수(m)를 입력하세요: "))

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