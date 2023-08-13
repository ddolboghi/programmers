import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(y, x):
    q = deque([(y, x)])
    check[y][x] = True
    seaList = []
    while q:
        py, px = q.popleft()
        sea = 0
        #인접한 0개수 세기
        for i in range(4):
            yy = py + dy[i]
            xx = px + dx[i]
            if 0<=yy<n and 0<=xx<m:
                if not graph[yy][xx]:
                    sea += 1
                #빙산 방문
                elif graph[yy][xx] and not check[yy][xx]:
                    check[yy][xx] = True
                    q.append((yy, xx))
        if sea>0:
            seaList.append((py, px, sea))
    for y, x, sea in seaList:
        graph[y][x] = max(0, graph[y][x]-sea)
    return 1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

year = 0
while ice:
    berg = 0
    check = [[False]*m for _ in range(n)]
    delList = []
    for y, x in ice:
        if graph[y][x] and not check[y][x]:
            berg += bfs(y, x)
        if graph[y][x] == 0:
            delList.append((y, x))
    if berg>1:
        print(year)
        break
    
    ice = sorted(list(set(ice) - set(delList)))
    year += 1
if berg<2:
    print(0)