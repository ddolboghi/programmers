from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
answer = [0]*(n+1)
visited = [False]*(n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def bfs(tree, v, visited):
    q = deque([v])
    visited[v] = True
    
    while q:
        p = q.popleft()
        for c in tree[p]: # p = 부모노드, c = 자식노드
            if not visited[c]:
                visited[c] = True
                answer[c] = p
                q.append(c)

bfs(tree, 1, visited)

for i in range(2, n+1):
    print(answer[i])