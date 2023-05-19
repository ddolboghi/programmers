def solution(participant, completion):
    sort_part=sorted(participant)
    sort_comp=sorted(completion)
    sort_comp.append('0')

    for i,j in zip(sort_part,sort_comp):
        if i!=j:
            answer=i
            break
    
    return answer