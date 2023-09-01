n = int(input())
stairs = [int(input()) for _ in range(n)]

if n<3:
    print(sum(stairs))
else:
    #dp는 stairs의 각 계단마다 해당 계단까지의 합의 최대값 저장
    #모든 계단을 저장하므로 마지막 계단을 출력하면됌
    dp = [0]*n
    dp[0] = stairs[0]
    dp[1] = dp[0] + stairs[1]
    dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])
    for i in range(3,n):
        dp[i] = max(stairs[i]+stairs[i-1]+dp[i-3], stairs[i]+dp[i-2])
    print(dp[-1])