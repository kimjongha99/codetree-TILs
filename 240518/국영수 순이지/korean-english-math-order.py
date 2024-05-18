n = int(input())

arr = []

for _ in range(n):
    name, subject1,subject2,subject3  = input().split()
    arr2 = [name, subject1,subject2,subject3]
    arr.append(arr2)

sort_arr = sorted(arr,key= lambda x:(x[0], x[1], x[2] ), reverse= True)

for name, subject1,subject2,subject3 in sort_arr:
    print(name, subject1,subject2,subject3)