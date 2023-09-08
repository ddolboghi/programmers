#최장증가수열(LIS) 응용문제
import sys
n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

dp = [0]*(n+1)
lis = 0
for i in line:
    dp[i] = dp[i-1] + 1
    lis = max(lis, dp[i])
print(n-lis)