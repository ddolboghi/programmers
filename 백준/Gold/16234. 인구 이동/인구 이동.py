from collections import deque

n, l, r = map(int, input().split())

land = [list(map(int, input().split())) for _ in range(n)]


dxy = ((0, -1), (0, 1), (-1, 0), (1, 0))

def bfs(start):
  # start: tuple ; (x, y)
  global check
  q = deque([start])
  check[start[1]][start[0]] = True
  uni = []
  uni_people = land[start[1]][start[0]]
  while q:
    x, y = q.popleft()

    for i in range(4):
      vx = x + dxy[i][0]
      vy = y + dxy[i][1]

      if 0<= vx < n and 0<= vy < n and not check[vy][vx] and l <= abs(land[y][x] - land[vy][vx]) <= r:
        check[vy][vx] = True
        uni.append((vx, vy))
        q.append((vx, vy))
        uni_people += land[vy][vx]
  
  if len(uni) < 1:
    return uni, 0
  
  uni.append(start)
  return uni, uni_people

answer = 0
while True:
  unis = []
  check = [[False] * n for _ in range(n)] 
  for i in range(n):
    for j in range(n):
      if not check[i][j]:
        uni, uni_people = bfs((j, i))
        if len(uni) > 0:
          unis.append([uni, uni_people//len(uni)])
  
  if len(unis) < 1:
    break;

  answer += 1
  
  for u in unis:
    for x, y in u[0]:
      land[y][x] = u[1]

print(answer)
