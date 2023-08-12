from collections import deque
n = int(input())
region = []
min_rain, max_rain = 100, 1
for _ in range(n):
    row = list(map(int, input().split()))
    max_rain = max(max_rain, max(row))
    region.append(row)

#region에서 가장 작은 원소부터 시작해서 가장 큰 원소까지가 rain의 범위
#차례대로 각 노드 방문하며 rain보다 작거나 같으면 값을 0으로 바꾸고
#rain의 반복마다 safe 카운트하고 그중 max값 출력
dx = [-1,1,0,0]
dy = [0,0,-1,1]

result = 0
for r in range(max_rain-1, -1, -1):
    safe = 0
    check = [[False for _ in range(n)] for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if not check[y][x] and r<region[y][x]:
                q = deque([(y, x)])
                check[y][x] = True
                safe += 1
                while q:
                    py, px = q.popleft()
                    for k in range(4):
                        yy = py + dy[k]
                        xx = px + dx[k]
                        
                        if 0<=yy<n and 0<=xx<n and not check[yy][xx] and r<region[yy][xx]:
                            check[yy][xx] = True
                            q.append((yy, xx))
    result = max(result, safe)
print(result)