n = int(input())
dp = [0, 0, 1, 1]
path = [[],[1], [2,1], [3,1]]
for i in range(4, n+1):
    temp = {}
    if i%3==0:
        temp[dp[i//3]+1] = i//3
    if i%2==0:
        temp[dp[i//2]+1] = i//2
    
    temp[dp[i-1]+1] = i-1
    min_ = min(temp.keys())
    dp.append(min_)
    path.append([i]+path[temp[min_]])
    
print(dp[n])
print(' '.join(map(str, path[n])))