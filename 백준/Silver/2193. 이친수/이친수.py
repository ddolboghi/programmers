n = int(input())
dp = [1,1]
for i in range(2,n):
    tmp = 0
    for j in range(i-1):
        tmp += dp[j]
    dp.append(tmp+1)
print(dp[n-1])