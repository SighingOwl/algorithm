n = int(input())
candies = [int(x) for x in input().split()]

win_count = 0
loss_count = 0
for i in range(n):
    order = candies[i] // 3
    remainder = candies[i] % 3
    
    if order % 2 == 0:
        if remainder == 0 or remainder == 2:
            loss_count += 1
        else:
            win_count += 1
    else:
        if remainder == 0 or remainder == 2:
            win_count += 1
        else:
            loss_count += 1
        
if loss_count == win_count:
    print('tie')
else:
    print(max(loss_count, win_count))