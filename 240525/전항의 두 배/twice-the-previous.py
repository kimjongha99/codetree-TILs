a, b =map(int, input().split())


ans = [a,b]

for i in range(8):
    ans.append(2*ans[i]+ans[i+1])



for ele in ans:
    print(ele , end=" ")