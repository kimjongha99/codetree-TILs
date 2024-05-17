n= int(input())

words = []

for _ in range(n):
    str= input()
    words.append(str)


group_dict = {}


for word in words:
    sorted_word_list  = sorted(word)
    sorted_word = ''
    for char in sorted_word_list:
        sorted_word += char

    if sorted_word in group_dict:
        group_dict[sorted_word]+=1
    else:
        group_dict[sorted_word]=1


print(max(group_dict.values()))