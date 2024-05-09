#  m1 ,d1 , m2 , d2 를 입력받음
m1, d1, m2, d2 = tuple(map(int, input().split()))

# 날짜를 입력받음
yoil = input()



# 1월부터 12월의 날짜 일수를 배열에 저장  [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 2월 윤년
month=[0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date= {
    'Mon' :1 ,
    'Tue': 2,
    'Wed': 3,
    'Thu': 4,
    'Fri': 5,
    'Sat': 6,
    'Sun ': 7,

}

def fuc1(m1, d1):
    sum_day =0
    for i in range(1,m1):
        sum_day += month[i]

    sum_day+=d1

    return sum_day


val = fuc1(m2,d2)- fuc1(m1,d1)



print(val//date[yoil])