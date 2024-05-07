start_h , start_m , end_h, end_m = map(int,input().split())


sum_min =0

while True:

    if start_h == end_h and start_m == end_m:
        break

    sum_min +=1
    start_m+=1

    if start_m ==60:
        start_h +=1
        start_m =0

print(sum_min)