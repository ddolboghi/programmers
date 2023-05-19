def solution(k, score):
    answer = []
    hof = []
    for i in range(0,len(score),1):
        if i < k:
            hof.append(score[i])
        else:
            if score[i] > min(hof):
                hof.remove(min(hof))
                hof.append(score[i])    
        answer.append(min(hof))
    return answer