def solution(numbers, target):
    return dfs(0, 0, numbers, target)

def dfs(idx, sum_, numbers, target):
    if idx == len(numbers):
        if sum_ == target:
            return 1
        else:
            return 0

    return dfs(idx+1, sum_ + numbers[idx], numbers, target) + dfs(idx+1, sum_ - numbers[idx], numbers, target)
        
    