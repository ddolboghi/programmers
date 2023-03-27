def solution(dartResult):    
    #S, D, T만 계산한 점수 저장
    score = []
    for i in range(len(dartResult)):
        if dartResult[i] in '0123456789':
            js = dartResult[i]
        elif dartResult[i-2:i] == '10':
            js = dartResult[i-2:i]
            
        if dartResult[i] == 'S':
            score.append(int(js))
        elif dartResult[i] == 'D':
            score.append(int(js)**2)
        elif dartResult[i] == 'T':
            score.append(int(js)**3)
        # print(js, score)
    # *, # 계산
    for i in range(len(dartResult)):
        if dartResult[i] == '*':
            if i<=3:
                score[0] = score[0] * 2
            elif 3<i<=5:
                score[0] = score[0] * 2
                score[1] = score[1] * 2
            else:
                score[1] = score[1] * 2
                score[2] = score[2] * 2
                
        elif dartResult[i] == '#':
            if i<=3:
                score[0] = score[0] * (-1)
            elif 3<i<=5:
                score[1] = score[1] * (-1)
            else:
                score[2] = score[2] * (-1)        
    # print(score)
    return sum(score)