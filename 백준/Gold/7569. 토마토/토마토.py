#도저히 안풀려서 정답 봄

import sys
from collections import deque
m, n, h = map(int, sys.stdin.readline().split())
box = []
q = deque()
for z in range(h):
    temp = []
    for y in range(n):
        temp.append(list(map(int, input().split())))
        for x in range(m):
            if temp[y][x] == 1:
                q.append((z,y,x))
    box.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

while q:
    pz, py, px = q.popleft()

    for i in range(6):
        yy = py + dy[i]
        xx = px + dx[i]
        zz = pz + dz[i]
        
        if 0<=zz and zz<h and 0<=yy and yy<n and 0<=xx and xx<m and box[zz][yy][xx]==0:    
            q.append((zz, yy, xx))
            box[zz][yy][xx] = box[pz][py][px] + 1
                                
day = 0                        
for p in box:
    for r in p:
        for c in r:
            if c == 0:
                print(-1)
                exit()
            else:
                day = max(day, c)
print(day-1)