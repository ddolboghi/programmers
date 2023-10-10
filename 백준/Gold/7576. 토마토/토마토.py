from collections import deque
m, n = map(int, input().split())
q = deque()
box = []
for i in range(n):
    temp = list(map(int, input().split()))
    box.append(temp)
    for j in range(m):
        if temp[j] == 1:
            q.append((i, j))
            
#고립된 구역은 가장 오래걸리는 날짜에 포함됨
#미리 익은 좌표 넣어놓고 시작해야 다른 익은 좌표에 영향 안받음

dx = [0,0,-1,1]
dy = [1,-1,0,0]

while q:
    y, x = q.popleft()

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]
        
        if 0<=xx<m and 0<=yy<n and box[yy][xx]==0:
            box[yy][xx] = box[y][x]+1
            q.append((yy, xx))

#print(box)
day = 0
for i in range(n):
    for j in range(m):
        if box[i][j] == 0:
            print(-1)
            exit()
        else:
            day = max(day, box[i][j])
print(day-1)