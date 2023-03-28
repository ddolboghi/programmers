def solution(k, m, score):
    
    answer_list = []
    sorted_list = sorted(score, reverse=True) 
    
    for i in range(0,len(sorted_list)//m,1):
        answer_list.append(min(sorted_list[i*m:(i+1)*m])*m)

    answer = sum(answer_list)
    
    return answer