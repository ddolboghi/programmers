from collections import deque
import sys

m, n =map(int, input().split())

fiber = [sys.stdin.readline().rstrip() for _ in range(m)]

outer = [int(i) for i in range(n) if fiber[0][i] == "0"]

# 한번 갔던 곳은 확인할 필요 없음

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))
check = [[False] * n for _ in range(m)]
def bfs(out):
  q = deque([(0, out)])
  
  check[0][out] = True


  while q:
    y, x = q.pop()

    if y == m-1 and fiber[y][x] == "0":
      return True

    for dx, dy in dxy:
      xx = x + dx
      yy = y + dy

      if 0<=xx<n and 0<=yy<m and fiber[yy][xx] == "0" and not check[yy][xx]:
        check[yy][xx] = True
        q.append((yy, xx))

  return False

result = 0

for out in outer:
  result += bfs(out)

print("YES") if result != 0 else print("NO")