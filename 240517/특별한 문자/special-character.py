word = input()

di ={}

for char in word:
    if char in di:
        di[char] +=1
    else:
        di[char] =1

di_list = list(di.items())

di_list.sort(key=lambda x:x[1],reverse=False)


if di_list[0][1] >=2 :
    print("None")
else:
    print(di_list[0][0])