arr1= ['apple','banana','grape','blueberry','orange']


ch1= input()
count =0 

for ele in arr1:
    for e in ele:
        if e == ch1:
            count +=1
            print(ele)
            break

print(count)