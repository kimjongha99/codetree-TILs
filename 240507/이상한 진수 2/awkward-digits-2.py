binary_string = input()

max_binary = binary_string
for i in range(len(binary_string)):
    if(len(binary_string)==0):
        print(0)
        break
    if binary_string[i] == '0':
        max_binary = binary_string[:i] + '1' + binary_string[i+1:]
        break
# 변경된 2진수 문자열을 10진수로 변환
max_value = int(max_binary, 2)

# 결과 출력
print(max_value)