n = int(input())
arr1 =[
]

for _ in range(n):
    str1 = input()
    arr1.append(str1)
    

count =0
count2 =0
for ele in arr1:
    count += len(ele)  # 문자열의 길이를 더함
    if ele[0] == 'a':
        count2+=1
        


print(count, count2)