n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]

dp = tri.copy()
for i in range(1,n):
    dp[i][0] = dp[i-1][0]+tri[i][0]#줄의 처음 숫자
    for j in range(1, len(tri[i])-1):
        dp[i][j] = max(dp[i-1][j-1]+tri[i][j], dp[i-1][j]+tri[i][j])
    dp[i][-1] = dp[i-1][-1]+tri[i][-1]#줄의 마지막 숫자
print(max(dp[-1]))