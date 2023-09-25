n = int(input())
dp = [1,1,1,1,1,1,1,1,1,1] # n=1일때 0~9까지 각 숫자에서 n자리일때 개수들

for i in range(1, n):
    temp = [dp[1]]    
    for j in range(1,9):
        temp.append(dp[j-1]+dp[j+1])
    temp.append(dp[8])
    # print(i, temp)
    dp = temp
print(sum(dp[1:])%1000000000)