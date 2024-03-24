from collections import deque
# 1. bfs로 먹을수 있는 물고기 찾기
# 2. 먹을수 있는 물고기 위치를 리스트에 넣기
# 3. 리스트를 y, x가 작은 순서대로 정렬
# 4. 가장 앞의 원소(물고기)가 있는 위치로 상어 위치 갱신하고 거리(시간) 누적
# 5. 1부터 반복, 리스트가 빌때까지
n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

start = []
for y in range(n):
  for x in range(n):
    if area[y][x] == 9:
      start.append(x)
      start.append(y)
      area[y][x] = 0

dxy = ((0, 1), (0, -1), (1, 0), (-1, 0))

def find_fish(start, shark):
  eatable = []
  check = [[False]*n for _ in range(n)]
  check[start[1]][start[0]] = True
  q = deque([start]) 
  while q:
    x, y, t = q.popleft()

    for dx, dy in dxy:
      xx = x + dx
      yy = y + dy
      
      if 0<=xx<n and 0<=yy<n and area[yy][xx]<=shark and not check[yy][xx]:
        # 지나갈수있고 방문하지 않았으면 q에 추가
        q.append([xx, yy, t+1])
        check[yy][xx] = True
        if 0<area[yy][xx]<shark:
          eatable.append([xx, yy, t+1])
  
  return eatable

start = start+[0] # 거리 측정 위해 0 추가
eatable = [start] # 반복문 시작 위한 더미 값
shark = 2 # 상어 크기
cnt = 0 # 성장마다 먹어야하는 마릿수
time = 0
while eatable:
  # print("start: ", start)
  eatable = find_fish(start, shark)
  if eatable:
    # 거리 가까운 곳 > y 작은 곳 > x 작은 곳
    sorted_eatable = sorted(eatable, key= lambda e: (e[2], e[1], e[0]))
    start = sorted_eatable[0] # 상어가 먹음
    area[start[1]][start[0]] = 0 # 먹었으면 크기 0으로 
    cnt += 1 # 먹은 마릿수 누적
    
    if cnt == shark:
      shark += 1
      cnt = 0

print(start[-1])