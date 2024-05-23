n = int(input())
i = 1

while True:
    i += 1
    n //= i
    if n <= 1:
        break

print(i)