n = int(input())
graph = [[0]*101 for _ in range(101)]

dxy = [[1, 0], [0, -1], [-1, 0], [0, 1]]

for i in range(n):
  x, y, d, g = map(int, input().split())
  graph[y][x] = 1

  curve = [d]
  for j in range(g):
    for k in range(len(curve)-1, -1, -1):
      curve.append((curve[k]+1) % 4)

  for c in curve:
    x += dxy[c][0]
    y += dxy[c][1]
    if 0 <= x < 101 and 0 <= y < 101:
      graph[y][x] = 1

answer = 0
for i in range(100):
  for j in range(100):
    if graph[i][j] * graph[i+1][j] * graph[i][j+1] * graph[i+1][j+1] == 1:
      answer += 1

print(answer)