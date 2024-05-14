n = int(input())

arr = [0]*201

point =100


def funR(x):
    global point
    for j in range(point,  point+x):
        arr[j] += 1
    point+=x


def funL(x) :
    global point
    for j in range(point , point-x,-1):
        arr[j] +=1
    point -= x


for i in range(n):
    x_str ,y_str = input().split()
    x = int(x_str)
    if y_str == 'R':
        funR(x)
    if y_str == 'L':
        funL(x)


count =0
for elem in arr:
    if elem >= 2:
        count+=1

print(count)