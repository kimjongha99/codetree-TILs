#  m1 ,d1 , m2 , d2 를 입력받음
m1, d1, m2, d2 = tuple(map(int, input().split()))

# 날짜를 입력받음
yoil = input()



# 1월부터 12월의 날짜 일수를 배열에 저장  [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 2월 윤년
month=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

DoW=0
ans=0





if date[DoW]==yoil:
    ans+=1
while True:

    if m1 == m2 and d1 == d2:
        print(ans)
        break



    d1 +=1
    DoW+=1


    if d1 > month[m1]:
        d1 =1
        m1 +=1


    if DoW>6:
        DoW =0
    if date[DoW] == yoil:
        ans+=1