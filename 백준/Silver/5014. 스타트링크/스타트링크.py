from collections import deque
tot, start, end, u, d = map(int, input().split())

q = deque([(start, 0)])
check = [False]*1000000
check[start-1] = True 
while q:
    v, cnt = q.popleft()
    if v == end:
        print(cnt)
        break
        
    args = []
    if v+u <= tot:
        args.append(v+u)
    if v-d >0:
        args.append(v-d)

    for i in args:
        if 1 <= i and i <=1000000 and not check[i-1]:
            check[i-1] = True
            q.append((i, cnt+1))

if v != end:
    print("use the stairs")