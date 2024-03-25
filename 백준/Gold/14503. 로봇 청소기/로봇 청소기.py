from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

D = [3, 0, 1, 2] # 서 북 동 남, D[d] = 반시계 90도 방향
backD = [2, 3, 0, 1] # 남 서 북 동 backD[d] = 후진 방향
dxy = ((0, -1), (1, 0), (0, 1), (-1, 0)) # 북 동 남 서, dxy[d'] 방향으로 이동

start = (c, r, d) # x, y, 방향
q = deque([start])
room[r][c] = 2
cnt = 1
while q:
  x, y, dd = q.popleft()

  # 청소 안한 곳 개수 세기
  unclean = 0
  for dx, dy in dxy:
    xx = x + dx
    yy = y + dy

    if room[yy][xx] == 0:
      unclean += 1

  # 청소할 곳 없으면 후진
  if unclean > 0:
    while True:
      dd = D[dd]
      gdx, gdy = x+dxy[dd][0], y+dxy[dd][1]
      if room[gdy][gdx] == 0:
        room[gdy][gdx] = 2
        q.append((gdx, gdy, dd))
        cnt += 1
        break
  # 청소할 곳 있으면 청소할 좌표 나올때까지 방향 회전하기
  else:
    bdx, bdy = dxy[backD[dd]]
    back_x = x + bdx
    back_y = y + bdy
    if 0<=back_x<m and 0<=back_y<n:
      if room[back_y][back_x] == 1:
        break
      else:
        q.append((back_x, back_y, dd))
    

print(cnt)