arr= [
    int(input())
    for _ in range(5)
]

cnt =0
for ele in arr:
    if ele %2 ==0:
        cnt+=1
print(cnt)