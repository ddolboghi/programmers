from collections import deque
n, m = map(int, input().split())
r, c, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def change(y, x, d):
    if d==0:
        d = 3
        x -= 1
    elif d==1:
        d = 0
        y -= 1
    elif d==2:
        d = 1
        x += 1
    else:
        d = 2
        y += 1
    return y, x, d
    
def back(y, x, d):
    if d==0:
        y += 1
    elif d==1:
        x -= 1
    elif d==2:
        y -= 1
    else:
        x += 1
    return y, x
    
def bfs(y, x, d):
    q = deque([(y, x, d)])
    room[y][x] = 2
    clean = 1
    while q:
        py, px, pd = q.popleft()
        empty = 0
        for i in range(4):
            yy = py + dy[i]
            xx = px + dx[i]
            if room[yy][xx] == 0:
                empty += 1
                
        #인접 0있으면 0나올때까지 방향전환
        if empty>0:
            while True:
                cy, cx, pd = change(py, px, pd)
                if room[cy][cx] == 0:
                    room[cy][cx] = 2
                    q.append((cy, cx, pd))
                    clean += 1
                    break
                    
        
        #인접 0없으면 후진
        else:
            by, bx = back(py, px, pd)
            if 0<=by<n and 0<=bx<m:
                if room[by][bx]==1:
                    break
                else:
                    q.append((by, bx, pd))
    return clean

print(bfs(r, c, d))