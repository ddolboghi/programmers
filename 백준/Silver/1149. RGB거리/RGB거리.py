### 인접한거끼리 같으면 안됌
n = int(input())
home = [list(map(int, input().split())) for _ in range(n)]

dp = []
temp = []
temp.append(min(home[1][0] + home[0][1], home[1][0]+home[0][2]))
temp.append(min(home[1][1] + home[0][0], home[1][1]+home[0][2]))
temp.append(min(home[1][2] + home[0][0], home[1][2]+home[0][1]))
dp.append(temp)
for i in range(2, n):
    temp = []
    temp.append(min(home[i][0] + dp[i-2][1], home[i][0]+dp[i-2][2]))
    temp.append(min(home[i][1] + dp[i-2][0], home[i][1]+dp[i-2][2]))
    temp.append(min(home[i][2] + dp[i-2][0], home[i][2]+dp[i-2][1]))
    dp.append(temp)
    
print(min(dp[-1]))