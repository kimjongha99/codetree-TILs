from datetime import datetime, timedelta

def count_specific_weekday(m1, d1, m2, d2, target_day):
    # 요일 맵핑
    weekday_map = {'Mon': 0, 'Tue': 1, 'Wed': 2, 'Thu': 3, 'Fri': 4, 'Sat': 5, 'Sun': 6}
    
    # 시작 날짜와 종료 날짜 설정
    start_date = datetime(2024, m1, d1)
    end_date = datetime(2024, m2, d2)
    
    # 특정 요일에 대한 숫자 매핑
    target_day_num = weekday_map[target_day]
    
    count = 0
    current_date = start_date
    
    # 시작 날짜부터 종료 날짜까지 반복하면서 요일 확인
    while current_date <= end_date:
        if current_date.weekday() == target_day_num:
            count += 1
        current_date += timedelta(days=1)
    
    return count

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

# 결과 계산
result = count_specific_weekday(m1, d1, m2, d2, target_day)

# 결과 출력
print(result)