n = int(input())
nums = list(map(int, input().split()))

dp = [0]*n
dp[0] = nums[0]
max_ = dp[0]
for i in range(1, len(nums)):
    if dp[i-1]+nums[i] > nums[i]:
        dp[i] = dp[i-1] + nums[i]
    else:
        dp[i] = nums[i]

    if max_ < dp[i]:
        max_ = dp[i]

print(max_)