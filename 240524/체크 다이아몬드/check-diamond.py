n = int(input())

# 위쪽 절반
for i in range(n):
    spaces = ' ' * (n - i - 1)
    stars = '* ' * (i + 1)
    print(spaces + stars)

# 아래쪽 절반
for i in range(n - 1):
    spaces = ' ' * (i + 1)
    stars = '* ' * (n - i - 1)
    print(spaces + stars)