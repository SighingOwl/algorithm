n,m = [int(x) for x in input().split()]

office = []
for i in range(m):
    office.append([int(x) for x in input().split()])

#n^2
check_i = [0 for i in range(m)]
check_j = [0 for j in range(n)]

for i in range(m):
    for j in range(n):
        if office[i][j] == 1:
            check_i[i] = 1
        elif office[i][j] == 2:
            check_j[j] = 1
        elif office[i][j] == 3:
            check_i[i] = 1
            check_j[j] = 1

print(check_i)
print(check_j)

count_i_0 = 0
count_j_0 = 0
for i in range(len(check_i)):
    if check_i[i] == 0:
        count_i_0 += 1

for i in range(len(check_j)):
    if check_j[i] == 0:
        count_j_0 += 1

print(count_i_0 * count_j_0)