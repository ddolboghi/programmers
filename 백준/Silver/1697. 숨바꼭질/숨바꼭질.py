from collections import deque
n, k = map(int, input().split())
cnt = -1
check = [False]*100001
q = deque()
q.append([[n]])
check[n-1] = True
while q:
    v = q.popleft()
    cnt += 1
    if k in v[0]:
        print(cnt)
        break
    
    for row in v:
        temp = []
        for i in row:
            if i-1>=0 and not check[i-2]:
                check[i-2] = True
                temp.append(i-1)
            if i+1 <= 100000 and not check[i]:
                check[i] = True
                temp.append(i+1)
            if 2*i <= 100000 and not check[2*i-1]:
                check[2*i-1] = True
                temp.append(2*i)

        q.append([temp])