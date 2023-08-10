n = int(input())

map_ = [list(map(int, input())) for _ in range(n)]

check = [[False for _ in range(n)] for _ in range(n)]

dy = [-1, 0, 0, 1]
dx = [0, 1, -1, 0]

apt = []
for y in range(n):
    for x in range(n):
        if map_[y][x]==1:
            #bfs
            map_[y][x] = 0
            queue = [(y, x)]
            apt_cnt = 1 #아파트 개수
            while queue:
                py, px = queue.pop(0)
                
                for i in range(4):
                    xx = px + dx[i]
                    yy = py + dy[i]
                    
                    if 0<=yy and yy<n and 0<=xx and xx<n and map_[yy][xx]==1:
                        map_[yy][xx] = 0
                        apt_cnt += 1
                        queue.append((yy, xx)) 
            apt.append(apt_cnt)


print(len(apt))
for a in sorted(apt):
    print(a)