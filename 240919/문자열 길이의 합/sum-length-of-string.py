n = int(input())
arr1 =[
]

for _ in range(n):
    str1 = input()
    arr1.append(str1)
    

count =0
count2 =0
for ele in arr1:
    for ele1 in ele:
        count +=1
        if ele1[0] == 'a':
            count2+=1
            


print(count, count2)