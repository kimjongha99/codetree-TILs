n, m = map(int, input().split())

arr = list(map(int,input().split()))

queries = list(map(int, input().split()))
di= {}

for elem in arr:
    if elem in di:
        di[elem]+=1
    else:
        di[elem]=1

# 각 질의에 대해 수열에서의 등장 횟수를 출력
result = []
for q in queries:
    result.append(di.get(q, 0))


# 결과 출력 (공백으로 구분)
print(' '.join(map(str, result)))