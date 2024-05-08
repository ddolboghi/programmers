import sys

n = int(input())
task = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]
task.sort(key=lambda x:-x[1])

visited = [False] * 1001
result = 0
for d, w in task:
  while d > 0 and visited[d]:
    d -= 1

  if d != 0:
    visited[d] = True
    result += w

print(result)