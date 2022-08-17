import sys
sys.setrecursionlimit(10000)

def dfs(s, d):
    visited[s] = 1
    
    for i in G[s]:
        if visited[i] == 0:
            dfs(i, d + 1)

n, m = [int(x) for x in input().split()]
G = [[] for i in range(n + 1)]
for i in range(m):
    u, v = [int(x) for x in input().split()]
    G[u].append(v)
    G[v].append(u)
    
visited = [0 for i in range(n + 1)]
components_count = 0

for i in range(1, n + 1):
    if visited[i] == 0:
        if not G[i]:
            components_count += 1
            visited[i] = 1
        else:
            dfs(i, 0)
            components_count += 1
    
print(components_count)