
def solution(numbers, target):     
    return dfs(target, numbers, 0, 0, 0)

def dfs(target, numbers, idx, sum, result):
    
    if idx >= len(numbers):
        if target == sum:
            result += 1
        return result
    
    return dfs(target, numbers, idx+1, sum + numbers[idx], result) + dfs(target, numbers, idx+1, sum - numbers[idx], result)
    
    
    
    
            
        