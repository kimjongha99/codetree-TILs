str1 = list(input())

str2 = list(input())


isTrue ="Yes"

str1.sort()
str2.sort()

if len(str1) != len(str2):
    isTrue ="No"
else:
    for i in range(len(str1)):
        if str1[i]!=str2[i]:
            isTrue = "No"
            break

print(isTrue)