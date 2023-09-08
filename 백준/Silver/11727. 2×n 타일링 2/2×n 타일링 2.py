n = int(input())
dp = [1]
for i in range(1,n):
    if i%2!=0:
        dp.append(dp[i-1]*2+1)
    else:
        dp.append(dp[i-1]*2-1)
print(dp[-1]%10007)