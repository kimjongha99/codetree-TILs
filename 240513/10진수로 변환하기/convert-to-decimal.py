arr = list(map(int,input()))

n =0

for i , val  in enumerate(reversed(arr)):
    n += val * (2**i)


print (n)