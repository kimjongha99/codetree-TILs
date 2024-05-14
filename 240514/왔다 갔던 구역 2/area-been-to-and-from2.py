n = int(input())

arr = [0]*201

point =101


def funR(x, point=point):
    for j in range(point,  point+x):
        arr[j] += 1
    point+=x


def funL(x ,point=point):
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

print(max(arr))