n = int(input())

arr = [
    [] for _ in range(30)
]

point = 15

ans=[0]*3
def funR(num):
    global point

    for i in range(point,point+num):
        arr[i].append('B')
    point += num

def funL(num):
    global point
    for i in range(point-1,point-num-1, -1):
        arr[i].append('W')
    point-=num

for _ in range(n):
    str_n , str_c = input().split()
    num = int(str_n)
    if str_c =='R':
        funR(num)
    if str_c == 'L':
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


for ele in ans:
    print(ele, end=" ")