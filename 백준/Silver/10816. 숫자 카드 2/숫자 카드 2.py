# 정답 봄
import sys
input = sys.stdin.readline

n = int(input())
ns = list(map(int, input().split()))
m = int(input())
ms = list(map(int, input().split()))

d = {}
for i in ns:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
        
for k in ms:
    item = d.get(k)
    if item == None:
        print(0, end=' ')
    else:
        print(item, end=' ')