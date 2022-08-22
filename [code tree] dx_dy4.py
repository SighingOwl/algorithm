def in_range(x, y, n):
    return 0 < x and x <= n and 0 < y and y <= n

n, t = [int(x) for x in input().split()]
marble = input().split()

dxs = [0, 1, -1, 0]
dys = [1, 0, 0, -1]

dir = {
    'R' : 0,
    'D' : 1,
    'U' : 2,
    'L' : 3
}

x = int(marble[0])
y = int(marble[1])
dir_num = dir[marble[2]]

for i in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny, n):
        dir_num = 3 - dir_num
    else:
        x, y = x + dxs[dir_num], y + dys[dir_num]

print(x, y)