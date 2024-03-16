from collections import deque

# 나이트 이동 좌표
move = (
  (1, -2), (-1, -2), 
  (2, -1), (2, 1), 
  (1, 2), (-1, 2), 
  (-2, -1), (-2, 1)
)

def knight(l, start, goal):
  # 나이트가 이동할수 있는 곳에 goal이 없다면 그곳은 재방문 안해도 됨
  # start: [start x, start y, move count]
  q = deque([start])
  check = [[False]*l for _ in range(l)]
  check[start[1]][start[0]] = True

  while q:
    x, y, cnt = q.popleft()

    if x == goal[0] and y == goal[1]:
      return cnt

    for dx, dy in move:
      mx = x + dx
      my = y + dy
      if 0<=mx<l and 0<=my<l and not check[my][mx]:
        check[my][mx] = True
        q.append((mx, my, cnt+1))
  return -1


for _ in range(int(input())):
  l = int(input())
  start = list(map(int, input().split())) + [0]
  goal = list(map(int, input().split()))
  print(knight(l, start, goal))