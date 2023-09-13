n = int(input())
scd = [list(map(int, input().split())) for _ in range(n)]
dp = [s[1] for s in scd]

for i in range(n):
    if n-i >= scd[i][0]:
        for j in range(i):
            if scd[j][0] <= i and i-j >= scd[j][0]:
                dp[i] = max(dp[i], dp[j]+scd[i][1])
    else:
        dp[i] = 0

print(max(dp))