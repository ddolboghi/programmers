import  sys

n = int(sys.stdin.readline())

dp = [0]*(n+1)
for i in range(1, n+1):
    t, p = map(int, sys.stdin.readline().rstrip().split())
    dp[i] = max(dp[i-1], dp[i])
    end_day = i+t-1
    if end_day <= n:
        dp[end_day] = max(dp[i-1]+p, dp[end_day])

print(dp[-1])