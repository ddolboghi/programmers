from collections import deque
n, m = map(int, input().split())
canvas = [list(map(int, input().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(start):
    q = deque()
    q.append(start)
    area = 1
    while q:
        y, x = q.popleft()
        canvas[y][x] = 0
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<=xx<m and 0<=yy<n and canvas[yy][xx]==1:
                q.append((yy, xx))
                area += 1
                canvas[yy][xx] = 0
    return area

max_area = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if canvas[i][j] == 1:
            area = bfs((i, j))
            cnt += 1
            if max_area < area :
                max_area = area
print(cnt)
print(max_area)