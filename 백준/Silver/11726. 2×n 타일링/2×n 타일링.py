n = int(input())
dp = [0,1,2]
for i in range(2, n):
    dp.append(dp[i]+dp[i-1])
if n<3:
    print(dp[n]%10007)
else:
    print(dp[-1]%10007)