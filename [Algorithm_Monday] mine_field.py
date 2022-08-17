M, N = [int(x) for x in input().split()]
grid = [[0 for j in range(M + 2)] for i in range(N + 2)]
for i in range(N):
    tmp = input()
    for j in range(M):
        grid[i + 1][j + 1] = tmp[j]

mine_field = [[] for i in range(N)]
for i in range(N):
    for j in range(M):
        if grid[i + 1][j + 1] == "*":
            mine_field[i].append(grid[i + 1][j + 1])
        else:
            mine_count = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if k == i + 1 and l == j + 1:
                        pass
                    else:
                        if grid[k][l] == '*':
                            mine_count += 1
            mine_field[i].append(mine_count)

for i in range(N):
    for j in range(M):
        if j == M - 1:
            print(mine_field[i][j], end="\n")
        else:
            print(mine_field[i][j], end="")