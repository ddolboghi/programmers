n, m, v = map(int, input().split())
d = dict({i:[] for i in range(1,n+1)})
for _ in range(m):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for i in d:
    d[i] = sorted(d[i])

def dfs(graph, start, visited, ans=[]):
    visited[start-1] = True
    ans.append(start)
    for i in graph[start]:
        if not visited[i-1]:
            dfs(graph, i, visited)
    return ans


def bfs(graph, start, visited, ans=[]):
    queue = [start]
    visited[start-1] = True
    
    while queue:
        v = queue.pop(0)
        ans.append(v)
        
        for i in graph[v]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = True
    return ans
                
print(' '.join(map(str, dfs(d, v, [False]*n))))
print(' '.join(map(str, bfs(d, v, [False]*n))))