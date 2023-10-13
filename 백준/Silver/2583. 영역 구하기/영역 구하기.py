from collections import deque
m, n, k = map(int, input().split())#행, 열, 직사각형 개수
rec = [list(map(int, input().split())) for _ in range(k)]

#직사각형이 채워진곳은 1, 아니면 0인 2차원 리스트
paper = []
for y in range(m):
    tmp = []
    for x in range(n):
        go = 0
        for r in rec:
           if r[0]<=x<r[2] and r[1]<=y<r[3]:
               go = 1
        tmp.append(go)
    paper.append(tmp)
# print(paper)

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    paper[y][x] = 1
    area = 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]

            if 0<=xx<n and 0<=yy<m and paper[yy][xx]==0:
                q.append((xx, yy))
                paper[yy][xx] = 1
                area += 1
    return area

cnt = 0
areaList = []
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            areaList.append(bfs(j, i))
            cnt += 1

print(cnt)
print(' '.join(map(str, sorted(areaList))))