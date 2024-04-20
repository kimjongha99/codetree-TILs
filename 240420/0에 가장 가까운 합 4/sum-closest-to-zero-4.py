num = int(input())

arr = list(map(int, input().split()))

arr.sort()

result = []
closest_sum = float('inf')

for i in range(len(arr) - 2):
    left = i + 1
    right = len(arr) - 1

    while left < right:
        current_sum = arr[i] + arr[left] + arr[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = [arr[i], arr[left], arr[right]]

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            break  # 추가된 부분: 정확히 0인 합을 찾으면 루프를 종료


for elem in result:
    print(elem, end=" ")