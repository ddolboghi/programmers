n, m = map(int, input().split())
num = list(map(int, input().split()))
ran = [list(map(int, input().split())) for _ in range(m)]

dp = [0, num[0]]
for i in range(1,n):
    dp.append(dp[i]+num[i])

for r in ran:
    print(dp[r[1]]-dp[r[0]-1])