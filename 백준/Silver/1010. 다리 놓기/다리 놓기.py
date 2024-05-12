dp = [[0]*31 for _ in range(31)]
dp[0] = [1]*(31)
for i in range(1, 31):
  for j in range(i, 31):
      dp[i][j] = dp[i-1][j-1] + dp[i][j-1]

for _ in range(int(input())):
  # m : 열, n : 행
  n, m = map(int, input().split())
  print(dp[n][m])