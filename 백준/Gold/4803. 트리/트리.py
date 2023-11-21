def isTree(node, parent):
    # 사이클에 포함된 노드는 인접 리스트에 모두 2번씩 나타남
    # q에 남아있는 노드가 이미 방문한 노드면 사이클이 포함되있음
    visited[node] = True
    for v in graph[node]:
        if v == parent: # 원소가 직전 노드면 건너뜀
            continue
        if visited[v]:
            return False
        if not isTree(v, node):
            return False
    return True

case = 0
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        cn, cm = map(int, input().split())
        graph[cn].append(cm)
        graph[cm].append(cn)
    
    treeCnt = 0
    visited = [False] * (n+1)
    for node in range(1, n+1):
        if visited[node]:
            continue
        if isTree(node, 0):
            treeCnt += 1
        
    case += 1
    if treeCnt > 1:
        print(f'Case {case}: A forest of {treeCnt} trees.')
    elif treeCnt == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: No trees.')