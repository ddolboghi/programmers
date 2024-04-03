from collections import deque
def solution(numbers, target):
    return bfs(numbers[0], target, numbers) + bfs(-numbers[0], target, numbers)

def bfs(start, target, numbers):
    count = 0
    q = deque([(start, 0)]) # (숫자, 계산 횟수)
    while q:
        n, cnt = q.popleft()
        
        if cnt == len(numbers)-1:
            if n == target:
                count += 1
            continue
        
        q.append((n + numbers[cnt+1], cnt+1))
        q.append((n - numbers[cnt+1], cnt+1))
    return count