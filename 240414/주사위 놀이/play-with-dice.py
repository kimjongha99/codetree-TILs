dice  =  list( map( int , input().split()  )  )


dice_number = [0]*7


for num in dice:
    dice_number[num]+=1


for i in range(1,7):
    cnt = dice_number[i]
    print(f'{i} - {cnt}')