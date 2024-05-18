n = int(input())
numbers = list(map(int, input().split()))

numbers.sort()


group_sums = []


for i in range(n):
    group_sum = numbers[i] + numbers[2 * n - 1 - i]
    group_sums.append(group_sum)

# 그룹의 합 중 최댓값을 출력
print(max(group_sums))