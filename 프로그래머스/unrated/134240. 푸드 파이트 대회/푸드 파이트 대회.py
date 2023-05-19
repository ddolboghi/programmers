def solution(food):
    
    list = [str(idx)*(i//2) for idx,i in enumerate(food) if i >= 2]
    
    answer=''.join(list)+'0'+''.join(list[::-1])
    
    return answer