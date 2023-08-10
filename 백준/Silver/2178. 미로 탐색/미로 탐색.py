n, m = map(int, input().split())
maze = []
for _ in range(n):
    maze.append(list(map(int, input())))


check = [[False for _ in range(m)] for _ in range(n)]

queue = []
queue.append((0, 0))

check[0][0] = True

#상, 하, 좌, 우
dy = [1,-1,0,0]
dx = [0,0,-1,1]

while queue:
    y, x = queue.pop(0)

    for i in range(4):
        yy = y + dy[i]
        xx = x + dx[i]

        if 0 <= yy and yy < n and 0 <= xx and xx < m and maze[yy][xx] == 1 and not check[yy][xx]:
            check[yy][xx] = True
            maze[yy][xx] += maze[y][x]
            queue.append((yy, xx))
print(maze[n-1][m-1])