from collections import deque

n = int(input())

if n == 0:
    print(0, 0)
    exit()

visited = {}  # visited[x] = (days, water)
q = deque()
q.append((0, 0, 0))  # (x, water, days)

min_days = float("inf")
min_water = float("inf")

while q:
    x, w, d = q.popleft()

    for nx, nw in [
        (x + 1, w + 1),
        (x * 3, w + 3),
        (x * x, w + 5),
    ]:
        if nx > n:
            continue

        if nx == n:
            if d + 1 < min_days:
                min_days = d + 1
                min_water = nw
            elif d + 1 == min_days:
                min_water = min(min_water, nw)
            continue

        # 방문하지 않았거나, 일수가 더 크거나, 일수가 같고 물 양이 더 많으면 방문 처리
        if (
            (nx not in visited)
            or (visited[nx][0] > d + 1)
            or (visited[nx][0] == d + 1 and visited[nx][1] > nw)
        ):
            visited[nx] = (d + 1, nw)
            q.append((nx, nw, d + 1))

print(min_days, min_water)
