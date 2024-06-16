def days_from_start(month, day):
    # 각 월의 일 수 정의 (윤년 고려)
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    for i in range(month - 1):
        days += days_in_month[i]
    days += day - 1
    return days

def calculate_weekday(days):
    # 2024년 1월 1일은 월요일이므로 0에 해당
    return (days % 7)

def count_specific_weekday(m1, d1, m2, d2, target_day):
    start_days = days_from_start(m1, d1)
    end_days = days_from_start(m2, d2)
    
    # 요일 맵핑
    weekday_map = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    target_day_num = weekday_map[target_day]
    
    count = 0
    for day in range(start_days, end_days + 1):
        if calculate_weekday(day) == target_day_num:
            count += 1
    
    return count

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

# 결과 계산
result = count_specific_weekday(m1, d1, m2, d2, target_day)

# 결과 출력
print(result)