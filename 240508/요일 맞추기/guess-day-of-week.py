m1, d1, m2, d2 = tuple(map(int, input().split()))

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
yoil = [ 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat','Sun']


# 일단 함수를 만들어야함
# 월과 일을 주면 1월1일부터  몇일이 흐른지 리턴
def func_day_count(m1, d1):
    sum_day = 0
    for i in range(1, m1):
        sum_day += num_of_days[i]

    sum_day += d1
    return sum_day


val =  func_day_count(m2, d2 ) -func_day_count(m1, d1)

while val < 0:
    val+=7


print(yoil[val%7])