n, m = [int(x) for x in input().split()]

office = [[0 for i in range(m + 2)] for i in range(n + 2)]
for i in range(n):
    tmp = [int(x) for x in input().split()]
    for j in range(m):
        office[i + 1][j + 1] = tmp[j]

count = 0
for i in range(n):
    for j in range(m):
        if office[i + 1][j + 1]  == 1:
            if office[i][j] == 1:
                if office[i + 1][j] == 2 and office[i][j + 1] == 2:
                    pass
                else:
                    count += 1
                    break
        
            if office[i][j + 2] == 1:
                if office[i + 1][j + 2] == 2 and office[i][j + 1] == 2:
                    pass
                else:
                    count += 1
                    break

            if office[i + 2][j] == 1:
                if office[i + 1][j] == 2 and office[i + 2][j + 1] == 2:
                    pass
                else:
                    count +- 1
                    break
            if office[i + 2][j + 2] == 1:
                if office[i + 2][j + 1] == 2 and office[i + 1][j + 2] == 2:
                    pass
                else:
                    count += 1
                    break

            if office[i][j + 1] == 1:
                count += 1
                break

            if office[i + 1][j] == 1:
                count += 1
                break

            if office[i + 1][j + 2] == 1:
                count += 1
                break

            if office[i + 2][j + 1] == 1:
                count += 1
                break

print(count)