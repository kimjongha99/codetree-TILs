n = int(input())

# 크게 범위를 설정하여 예외 상황 방지
MAX_K = 15000
arr = [[] for _ in range(2 * MAX_K + 1)]
point = MAX_K  # 중간 지점을 시작점으로 설정

ans = [0, 0, 0]  # [white, black, gray]

def funR(num):
    global point
    for i in range(point, point + num):
        arr[i].append('B')
    point += num - 1  # 마지막에 칠한 타일에 위치

def funL(num):
    global point
    for i in range(point, point - num, -1):
        arr[i].append('W')
    point -= num - 1  # 마지막에 칠한 타일에 위치

for _ in range(n):
    str_n, str_c = input().split()
    num = int(str_n)
    if str_c == 'R':
        funR(num)
    elif str_c == 'L':
        funL(num)


for row in arr:
    if len(row)>0:
        if len(row)>=4:
            ans[2] += 1
        else:
            if row.pop() == 'W':
                ans[0] +=1
            else:
                ans[1] +=1


for elem in ans:
    print(elem, end=" ")