a , b = map(int,input().split())

ans =1

for i in range(1, b+1):
    if i%4==0:
        ans*=i
    
print(ans)