def solution(nums):
    
    if (len(nums)//2)>=len(set(nums)):
        answer=len(set(nums))
    else:
        answer=len(nums)//2
    return answer