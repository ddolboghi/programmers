import collections
def solution(lottos, win_nums):
    answer = []
    rank = {6:1, 5:2, 4:3, 3:4, 2:5}
    counter = set(lottos) & set(win_nums)
    zero = lottos.count(0)
    
    b = (len(list(counter)) + zero)
    w = len(list(counter))
    
    if b < 2 :
        answer.append(6)
    else :
        answer.append(rank[b])
    
    if w < 2 :
        answer.append(6)
    else :
        answer.append(rank[w])
    
    return answer