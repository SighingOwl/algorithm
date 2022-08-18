n, m = [int(x) for x in input().split()]
grid = []
for i in range(n):
    grid.append([int(x) for x in input().split()])

happy = 0
for i in range(n):
    tmp_count = 0
    for j in range(n):
        if j == 0:
            tmp_count += 1
        elif grid[i][j] == grid[i][j - 1]:
            tmp_count += 1
        else:
            tmp_count = 1

        if tmp_count >= m:
            happy += 1
            break

for i in range(n):
    tmp_count = 0
    for j in range(n):
        if j == 0:
            tmp_count += 1
        elif grid[j][i] == grid[j - 1][i]:
            tmp_count += 1
        else:
            tmp_count = 1

        if tmp_count >= m:
            happy += 1
            break

print(happy)