n = int(input())
num = []
for i in range(n):
	num.append(int(input()))

count = 0
for i in range(n):
	square_root = num[i]**(1/2)
	
	if square_root == int(square_root):
		count += 1
		
print(count)