start_m , start_d , end_m, end_d = map(int,input().split())


month_list = [0,31,28,31,30,31,30,31,30,31,30,31,30]

sum_day=0

while True:

    if start_m == end_m and start_d ==  end_d:
        break

    start_d+=1
    sum_day+=1

    if start_d > month_list[start_m]:
        start_d=0
        start_m+=1

print(sum_day-1)