n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = dict({i:[] for i in range(1,n+1)})
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*n
result = []
def dfs(start, cnt):
    cnt += 1
    visited[start-1] = True
    
    if start == end:
        result.append(cnt-1)
        
    for i in graph[start]:
        if not visited[i-1]:
            dfs(i, cnt)
            
dfs(start, 0)
if not result:
    print(-1)
else:
    print(result[0])