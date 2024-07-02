n = int(input())  # 블록의 개수 입력

# 블록 높이 리스트 입력 (리스트 컴프리헨션을 사용하여 수정)
blocks = [
    int(input())
    for _ in range(n)
]

count_block = sum(blocks)  # 모든 블록의 높이 합계

avg = count_block / n  # 평균 높이 계산 (소수점을 고려한 나눗셈)

ans = 0  # 결과를 저장할 변수

for block in blocks:  # 각 블록에 대해 반복
    if block > avg:  # 블록 높이가 평균보다 높으면
        ans += block - avg  # 높이 차이를 결과에 더함

print(int(ans))  # 결과 출력 (정수로 변환하여 출력)