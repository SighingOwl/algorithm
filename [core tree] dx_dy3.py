def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

n = int(input())
grid = []
for i in range(n):
    grid.append([int(x) for x in input().split()])

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

target = 0
for i in range(n):
    for j in range(n):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = j + dx, i + dy
            if in_range(nx, ny, n) == True and grid[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            target += 1

print(target)    