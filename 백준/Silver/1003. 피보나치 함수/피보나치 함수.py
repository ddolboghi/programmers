#print되는 0, 1의 개수 

t = int(input())
case = [int(input()) for _ in range(t)]

for c in case:
    dp = [[1,0],[0,1]]
    if c>1:
        for i in range(2, c+1):
            dp.append([dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]])
        print(' '.join(map(str, dp[c])))
    else:
        print(' '.join(map(str, dp[c])))