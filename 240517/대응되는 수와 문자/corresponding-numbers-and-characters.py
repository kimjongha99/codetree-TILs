n ,m = map(int,input().split())

di_str ={}
di_num ={}
for i in range(1,n+1):
    x = input()
    di_str[x] = i
    di_num[i] = x




for _ in range(m):
    x = input()
    if x.isdigit():
        x = int(x)
        print(di_num[x])

    else:
        print(di_str[x])