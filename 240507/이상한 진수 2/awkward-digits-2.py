binary_string = input()
if binary_string == "1":
    # 입력이 "1"인 경우는 "0"으로 바꿔서 출력
    max_value = 0
else:
    # 첫 번째 '0'을 '1'로 변경하여 최댓값을 찾기
    max_binary = binary_string
    for i in range(len(binary_string)):
        if binary_string[i] == '0':
            max_binary = binary_string[:i] + '1' + binary_string[i+1:]
            break

    # 변경된 2진수 문자열을 10진수로 변환
    max_value = int(max_binary, 2)

# 결과 출력
print(max_value)