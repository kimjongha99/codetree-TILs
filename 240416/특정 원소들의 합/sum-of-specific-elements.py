arr_2d = [
   list(map( int , input().split()))
    for _ in range(4)
]


sum_val=0
for i in range(4):
    for j in range(4):
        if i==0:
            sum_val+= arr_2d[i][0]
            break
        if i==1:
            sum_val += arr_2d[i][0]
            sum_val += arr_2d[i][1]
            break
        if i == 2:
            sum_val += arr_2d[i][0]
            sum_val += arr_2d[i][1]
            sum_val += arr_2d[i][2]
            break
        if i == 3:
            sum_val += arr_2d[i][0]
            sum_val += arr_2d[i][1]
            sum_val += arr_2d[i][2]
            sum_val += arr_2d[i][3]
            break


print(sum_val)