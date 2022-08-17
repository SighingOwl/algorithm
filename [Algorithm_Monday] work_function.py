n, m = [int(x) for x in input().split()]

result = 0
DP = [0 for i in range(m + 1)]
for i in range(1, m + 1):
    if i == 1 or i == 2:
        DP[i] = 1
    elif i % 2 == 0:
        DP[i] = DP[i // 2] + 1
    elif i % 2 == 1:
        DP[i] = DP[(i + 1) // 2] + 2

    if i >= n:
        result += DP[i] 

print(result)
