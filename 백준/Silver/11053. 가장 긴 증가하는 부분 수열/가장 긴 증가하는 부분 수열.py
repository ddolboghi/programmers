n = int(input())
nums = list(map(int, input().split()))
dp = [1]*n 
# 1로 채운 이유는 이전 숫자들보다 작거나 같으면 
# 거기서부터 다시 길이 세기 위해서

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))