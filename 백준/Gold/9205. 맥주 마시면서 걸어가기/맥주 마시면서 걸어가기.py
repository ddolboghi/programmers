from collections import deque
def bfs(start):
    q = deque([start])
    while q:
        x, y = q.popleft()
        if abs(x-e[0]) + abs(y-e[1]) <= 1000:
            print("happy")
            return
        #거리가 1000보다 크면 편의점 들르기
        for i in range(n):
            if not check[i]:
                cx, cy = cu[i]
                if abs(x-cx) + abs(y-cy) <= 1000:
                    q.append(cu[i])
                    check[i] = 1
    
    #처음부터 거리가 1000보다 크고 편의점이 없을때
    #최종적으로 거리가 1000보다 클때
    print("sad")
    return

t = int(input())
for i in range(t):
    n = int(input())
    s = tuple(map(int, input().split()))
    cu = [tuple(map(int, input().split())) for j in range(n)]
    e = tuple(map(int, input().split()))
    check = [0 for i in range(n+1)] #s제외
    bfs(s)