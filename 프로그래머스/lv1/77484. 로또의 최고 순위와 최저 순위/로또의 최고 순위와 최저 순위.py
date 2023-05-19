def solution(lottos, win_nums):

    cross = len(set(lottos)&set(win_nums))
    zeros = len([i for i in lottos if i == 0])
    
    dict1 = {0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    
    answer = [dict1[cross+zeros],dict1[cross]]
    return answer