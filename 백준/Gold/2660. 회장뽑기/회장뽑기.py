import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    visited = [0] * (n+1)
    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        for friend in graph[v]:
            if not visited[friend]:
                q.append(friend)
                visited[friend] = visited[v]+1
    
    return max(visited)-1


scores = [bfs(i) for i in range(1, n+1)]

minScore = min(scores)
print(minScore, scores.count(minScore))
candidates = ""
for i in range(n):
    if scores[i] == minScore:
        print(i+1, end=" ")