# 1개의 사이클에서 끊는 연산은 1회
import sys

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

n, m = map(int, sys.stdin.readline().split())
parent = [i for i in range(n+1)]

cycleSplitCnt = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    roota, rootb = find(a), find(b)
    if roota == rootb:
        cycleSplitCnt += 1 
        continue
    if roota > rootb: # 항상 큰 루트 노드에 합쳐지도록 단순히 값만 스와핑함
        roota, rootb = rootb, roota

    parent[rootb] = roota

for i in range(1, n+1):
    find(i)


groupMergeCnt = len(set(parent[1:])) - 1
print(groupMergeCnt + cycleSplitCnt)