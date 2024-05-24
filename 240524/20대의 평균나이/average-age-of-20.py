sum_age =0
count = 0
while True:
    age = int(input())
    if age < 20 or age > 29:
        break

    sum_age+=age
    count +=1


print(f"{sum_age/count:0.2f}")