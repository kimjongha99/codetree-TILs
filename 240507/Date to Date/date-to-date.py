start_m , start_d , end_m, end_d = map(int,input().split())


num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum_day=0


if start_m == end_m and start_d == end_d:
    print(1)
else:
    while True:
        if start_m == end_m and start_d == end_d:
            break

        start_d+=1
        sum_day+=1

        if start_d > num_of_days[start_m]:
            start_d=0
            start_m+=1

    print(sum_day)