t = int(input())
ns = [int(input()) for _ in range(t)]

n = max(ns)
dp = [1,1,1,2,2]
for i in range(n):
    dp.append(dp[i] + dp[i+4])

for k in ns:
    print(dp[k-1])