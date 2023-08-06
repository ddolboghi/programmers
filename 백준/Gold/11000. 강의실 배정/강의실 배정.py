import sys
import heapq

n = int(input())
lec = [list(map(int, input().split())) for _ in range(n)]

lec = sorted(lec, key=lambda x: (x[0], x[1]))

rooms = []
heapq.heappush(rooms, lec[0][1])
for i in range(1,n):
    if rooms[0] > lec[i][0]:
        heapq.heappush(rooms, lec[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms, lec[i][1])

print(len(rooms))