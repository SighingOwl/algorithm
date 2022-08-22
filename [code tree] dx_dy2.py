cmd = input()

dx = [1, 0, -1, 0]
dy = [0, -1, 0 , 1]

x = 0
y = 0
dir = 3
for i in range(len(cmd)):
    if cmd[i] == 'R':
        dir = (dir + 1) % 4
    elif cmd[i] == 'L':
        dir = (dir + 3) % 4
    else:
        x, y = x + dx[dir], y + dy[dir]

print(x, y)