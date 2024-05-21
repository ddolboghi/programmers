r, c, k = map(int, input().split())

graph = [list(input()) for _ in range(r)]

dxy = ((0, -1), (0, 1), (-1, 0), (1, 0))

cnt = 0 
def dfs(x, y, dis):
  global cnt

  if x == c-1 and y == 0 and dis == k:
    cnt += 1
  else:
    graph[y][x] = "T"
    for i in range(4):
      vx = x + dxy[i][0]
      vy = y + dxy[i][1]
      if 0 <= vx < c and 0 <= vy < r and graph[vy][vx] == ".":
        graph[vy][vx] = "T"
        dfs(vx, vy, dis+1)
        graph[vy][vx] = "."

dfs(0, r-1, 1)
print(cnt)