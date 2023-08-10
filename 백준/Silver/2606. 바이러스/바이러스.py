n = int(input())
m = int(input())

graph = dict({i:[] for i in range(1,n+1)})
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

n = len(graph)
visited = [False]*n

def dfs(graph, start, visited):
    visited[start-1] = True
    for i in graph[start]:
        if not visited[i-1]:
            dfs(graph, i, visited)
    
    return visited.count(True)-1

print(dfs(graph, 1, visited))