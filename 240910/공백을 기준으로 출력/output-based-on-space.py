str1 = input()

str2 = input()


str3 =str1+str2
result = ''

for ele in str3:
    if ele ==' ':
        continue
    result += ele  # 문자열 연결


print(result)