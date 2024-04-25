tc = int(input())


arr= list(map(int,input().split()))

myarr = sorted(arr)


isexist = False

low2 = 0


for elem in myarr:
    if elem != arr[0]:
        low2 = elem
        isexist = True
        break

if isexist == False:
    print(-1)
    sys.exit()


ansidx = -1

for idx , elem  in enumerate(arr):
  if elem == low2:
        # 2번째로 작은 숫자가 여러 개 있을 때
        if ansidx != -1:
            print(-1)
            sys.exit()

        ansidx = idx

print(ansidx + 1)