s, e = [int(x) for x in input().split()]

result = 0
for i in range(s, e + 1):
	if i >= 10 and i < 100:
		tmp1 = i // 10
		tmp2 = i % 10
		result += tmp1 * tmp2
	elif i > 100:
		tmp1 = i // 100
		i %= 100
		tmp2 = i // 10
		tmp3 = i % 10
		result += tmp1 * tmp2 * tmp3
		
print(result)