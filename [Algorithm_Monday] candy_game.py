t = int(input())
candies = [int(x) for x in input().split()]

win_count = 0
for i in range(t):
	candy = candies[i]
	order = candy // 3
	remainder = candy % 3
	
	if order % 2 == 0:
		if remainder == 1:
			win_count += 1
	else:
		if remainder == 0 or remainder == 2:
			win_count += 1

loss_count = t - win_count

if loss_count == win_count:
	print("tie")
else:
	print(max(win_count, loss_count))

