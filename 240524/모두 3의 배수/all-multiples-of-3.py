arr= [
    int(input())
    for _ in range(5)
]

isTrue= 1

for ele in arr:
    if ele%3==0:
        isTrue =1
    else:
        isTrue=0
        break

print(isTrue)