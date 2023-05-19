def solution(survey, choices):
    answer = ''
    # choice:성격유형점수
    score = {1:3,2:2,3:1,4:0,5:1,6:2,7:3}
    d = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for s, c in zip(survey, choices):
        if c < 4:
            d[s[0]] += score[c]
        elif c > 4:
            d[s[1]] += score[c]
    # print(d)
    if d['R'] >= d['T']:
        answer += 'R'
    else:
        answer += 'T'
    if d['C'] >= d['F']:
        answer += 'C'
    else:
        answer += 'F'
    if d['J'] >= d['M']:
        answer += 'J'
    else:
        answer += 'M'
    if d['A'] >= d['N']:
        answer += 'A'
    else:
        answer += 'N'
    return answer