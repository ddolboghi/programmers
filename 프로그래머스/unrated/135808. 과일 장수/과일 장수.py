def solution(k, m, score):
    answer = 0
    #sorted score[i:j]
    #k=len(score)//m
    #i= m*range k
    sc=sorted(score, reverse=True)
    # print(sc)
    for x in range(0,len(score)//m):
        i, j = m*x, m + m*x
        if len(sc[i:j]) == m:
            # print(sc[i:j], i, j, x)
            answer += min(sc[i:j]) * len(sc[i:j])
        else:
            continue
    return answer