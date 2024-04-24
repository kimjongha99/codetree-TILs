tc = int(input())

arr= [
     input().split()
     for _ in range(tc)
]



score_A , score_B = 0,0
ans = 0 


def checK_socre(a, b):
    if a> b:
        return 1
    elif b>a:
        return 2
    else:
        return 3





for stu, value in arr:
    value = int(value)
    if stu =="A":
        if checK_socre(score_A,score_B) != checK_socre(score_A+value , score_B):
            ans+=1
        
        score_A+=value
    
    else:
        if checK_socre(score_A,score_B) != checK_socre(score_A , score_B+value):
            ans+=1
        
        score_B+=value


print(ans)