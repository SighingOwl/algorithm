n = int(input())
statistic = []
for i in range(n):
    statistic.append([int(x) for x in input().split()])

A_plus_count = 0
for i in range(n):
    A_plus = statistic[i][0] * (statistic[i][2] / 100)
    if statistic[i][1] > A_plus:
        continue

    for j in range(5, 5 + statistic[i][3]):
        if statistic[i][j] <= statistic[i][4]:
            break
        elif j == 5 + statistic[i][3] - 1 and statistic[i][j] > statistic[i][4]:
            A_plus_count += 1

if A_plus_count == n:
    print(1)
else:
    print(0)