import sys
input = sys.stdin.readline
m, n = map(int, input().split())
d = {}
for _ in range(m):
    planets = list(map(int, input().split()))
    sorted_planets = sorted(list(set(planets)))#같은 행성은 한번만 세기?
    rank = {sorted_planets[i]:i for i in range(len(sorted_planets))}#정렬된 값:인덱스
    vector = tuple(rank[i] for i in planets)#기존 값 -> 정렬됐을때 인덱스값으로 변환
    d[vector] = d.get(vector, 0) + 1

# n개 중 2개씩 묶어야하므로 nC2, 중복 제외
sum = 0
for i in d.values():
    sum += (i*(i-1))//2
print(sum)