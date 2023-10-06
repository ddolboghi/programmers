n = int(input())
m = int(input())
vip = [int(input()) for _ in range(m)]


# dp[k] = 연속된 좌석들이 k개 있을때 앉을 수 있는 경우의 수
# k >= 3 이면 dp[k] = dp[k-1] + dp[k-2]
if n > 1:
    ans = 1
    dp = [0]*(n+1)
    dp[1], dp[2] = 1, 2
    for k in range(3,n+1):
        dp[k] = dp[k-1] + dp[k-2]

    cnt = 0
    for i in range(1,n+1):
        if i in vip:
            if cnt != 0:
                ans *= dp[cnt]
            cnt = 0
        else:
            cnt += 1
    
        if i == n and n not in vip:
            ans *= dp[cnt]
    
    print(ans)
else:
    print(n)