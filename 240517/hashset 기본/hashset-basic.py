n = int(input())

s1 = set()

for _ in range(n):
    str, n = input().split()

    if str == 'find':
        if n in s1:
            print('true')
        else:
            print('false')

    elif str == 'add':
        s1.add(n)
    elif str == 'remove':
        s1.remove(n)