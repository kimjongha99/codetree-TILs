MIN_INF = -float('inf')


tc = int(input())

di ={}

for i in range(tc):
    str = input()
    if str in di:
        di[str] +=1
    else:
        di[str] = 1

max_val = MIN_INF
for ele in di:
    max_val = max(di[ele],max_val)



print(max_val)