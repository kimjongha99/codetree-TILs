arr = list(input())

# ( 의 개수를 저장하는 변수를 만든다
# ) 의 개수를 저장하는 변수를 만든다.

# for문으로 arr 를 순회하며  ( 이면  ( 변수에 +1 , ) 이면 ) 변수에 +1을한다.
# 그리고 더 작은 값을 제곱을하여 출력한다.
x =0
y =0

for elem in arr:
    if elem == '(':
        x +=1
    else:
        y+=1


min_val = min(x,y)

print(min_val**2-1)