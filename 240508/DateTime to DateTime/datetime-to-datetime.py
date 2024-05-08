end_d, end_h, end_m = map(int,input().split())

start_d = 11
start_h = 11
start_m = 11

sum_min=0


while True:

    if start_d == end_d and start_h == end_h and start_m == end_m:
        break


    sum_min+=1
    start_m +=1


    if start_m == 60:
        start_h +=1
        start_m =0


    if start_h == 24:
        start_d+=1
        start_h = 0


print(sum_min)