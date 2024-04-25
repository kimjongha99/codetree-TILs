import sys

# 변수 선언 및 입력
n = int(input())
a = list(map(int, input().split()))

# 새로운 배열을 만들어 정렬하고
# 2번째로 작은 숫자를 찾아냅니다.
myarr = sorted(a)

# isexist : 2번째로 작은 숫자가 존재하면 true
isexist = False
low2 = 0
for elem in myarr:
    # 가장 처음으로 myarr[0]과 다른 숫자는
    # 2번째로 작은 숫자라고 할 수 있습니다.
    if elem != myarr[0]:
        low2 = elem
        isexist = True
        break

# 2번째로 작은 숫자가 존재하지 않을 때
if isexist == False:
    print(-1)
    sys.exit()

ansidx = -1
for idx, elem in enumerate(a):
    if elem == low2:
        # 2번째로 작은 숫자가 여러 개 있을 때
        if ansidx != -1:
            print(-1)
            sys.exit()

        ansidx = idx

print(ansidx + 1)