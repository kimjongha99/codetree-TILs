a, b =map(int, input().split())
ans =[]

while True:

    if a <= 1:
        break

    ans.append(a%b)
    a = a // b


di ={}

for ele in ans:
    if ele in di:
        di[ele] +=1
    else:
        di[ele]=1


result = 0
for val in di.values():
    result += val**2

print(result)