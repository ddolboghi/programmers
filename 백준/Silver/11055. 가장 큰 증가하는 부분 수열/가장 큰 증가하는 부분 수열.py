# max함수로 값을 계속 바꾸는 아이디어
n = int(input())
nums = list(map(int, input().split()))

# dp = 각 원소로 끝나는 부분 수열의 합
dp = nums.copy() 

for i in range(n):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[i], dp[j]+nums[i])
            
print(max(dp))