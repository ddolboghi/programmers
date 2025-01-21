n, s = map(int, input().split())
m = int(input())
time = [int(input()) for _ in range(m)]

def eat(t):
  cnt = 0
  for i in range(m):
    cnt += t // time[i] + 1
  return cnt

start, end = 0, n-s
res = 0
while start <= end:
  mid = (start + end) // 2
  if eat(mid) >= n-s:
    res = mid
    end = mid - 1
  else:
    start = mid + 1

ans = 0
soboru = 0
if res == 0: soboru = 0
else: soboru = eat(res-1)
for i in range(m):
  if res % time[i] == 0 and soboru < n-s:
    ans = i + 1
    soboru += 1
print(ans)