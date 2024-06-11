def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

def season_check(month):
    if 3 <= month <= 5:
        return "Spring"
    elif 6 <= month <= 8:
        return "Summer"
    elif 9 <= month <= 11:
        return "Fall"
    else:
        return "Winter"


year, month, day = map(int, input().split())




# 이제 해야할것
# 입력받은 년도가 윤년인지 아닌지 if문 친다.
# 만약 윤년이면?
# 월을 확인해서
  #2월이면?
     #일의 숫자가 29가 넘는다? 그럼 -1 출력
  #2월이 아니면?
     # season_check 계절출력

#만약 윤년이 아니면?
# season_check 계절출력


# 각 월의 최대 일수 계산
if month == 1:
    max_day = 31
elif month == 2:
    if leap_year(year):
        max_day = 29
    else:
        max_day = 28
elif month == 3:
    max_day = 31
elif month == 4:
    max_day = 30
elif month == 5:
    max_day = 31
elif month == 6:
    max_day = 30
elif month == 7:
    max_day = 31
elif month == 8:
    max_day = 31
elif month == 9:
    max_day = 30
elif month == 10:
    max_day = 31
elif month == 11:
    max_day = 30
elif month == 12:
    max_day = 31
else:
    max_day = -1

# 날짜 유효성 검사
if month < 1 or month > 12 or day < 1 or day > max_day:
    print(-1)
else:
    print(season_check(month))