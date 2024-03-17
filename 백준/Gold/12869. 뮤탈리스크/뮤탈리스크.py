from collections import deque
from itertools import permutations

n = int(input())
hps = list(map(int, input().split()))

# bfs
# 6가지 경우의 수 -> 순열
# 체력(check)은 3차원 배열로 표현, 원소는 거리
# 시작점은 주어진 scv의 체력
# n < 3일때 0을 추가해서 3개로 맞춰야 3차원 배열로 계산 가능

for _ in range(3-n):
  hps.append(0)

check = [[[0] * 61 for _ in range(61)] for _ in range(61)]

# hps의 모든 원소가 0이 될때까지 bfs 돌기
# 6가지 경우를 모두 계산하고 방문하지 않은 곳만 가기
# check에 이전 방문한 곳의 거리 +1씩 누적
q = deque([hps])
while q:
  z, y, x = q.popleft()
  
  if z + y + x == 0:
    print(check[z][y][x])
    break

  for p in permutations([9, 3, 1], 3):
    xx = max(x-p[0], 0)
    yy = max(y-p[1], 0)
    zz = max(z-p[2], 0)
  
    if not check[zz][yy][xx]:
      check[zz][yy][xx] = check[z][y][x] + 1
      q.append([zz, yy, xx])
