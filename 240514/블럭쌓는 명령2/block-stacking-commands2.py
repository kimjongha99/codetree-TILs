n , k  = map(int,input().split())

arr= [0]*(n+1)

def func1(x, y):
    for i in range(x, y+1):
        arr[i] += 1




for _ in range(k):
    x ,y = map(int,input().split())
    func1(x,y)


print(max(arr))