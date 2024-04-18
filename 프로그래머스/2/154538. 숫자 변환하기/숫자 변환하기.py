from collections import deque

def solution(x, y, n):
    answer = 0
    q = deque([(x, 0)]) # 시작값, 연산횟수
    check = [False] * 1000001
    while q:
        xx, cnt = q.popleft()
        if xx == y:
            return cnt
        if xx < y and not check[xx]:
            check[xx] = True
            q.extend([(xx+n, cnt+1), (xx*2, cnt+1), (xx*3, cnt+1)])
    return -1