n = int(input())
lec = [list(map(int, input().split())) for _ in range(n)]

start_times = sorted([x[0] for x in lec])
end_times = sorted([x[1] for x in lec])

i = 0
cnt = 0
for s in start_times:
    if s >= end_times[i]:
        i += 1
    else:
        cnt += 1
        
print(cnt)