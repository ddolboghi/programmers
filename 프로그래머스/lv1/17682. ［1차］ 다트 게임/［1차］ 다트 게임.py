def solution(dartResult):
    
    sdt = {'S': 1, 'D': 2, 'T': 3}
    scores = [str(x) for x in range(0,10,1)]
    pri_jumsu = []
    storing = ''
    
    for c in dartResult:
        
        if c in scores:
            storing += c
        elif c in sdt:
            pri_jumsu.append(int(storing)**sdt[c])
            storing = ''
        elif c == '*':
            if len(pri_jumsu)>=2:  # list out of range 문제
                pri_jumsu[-2]=pri_jumsu[-2]*2
            pri_jumsu[-1]=pri_jumsu[-1]*2
        elif c == '#':
            pri_jumsu[-1] *= -1

    answer = sum(pri_jumsu)
    return answer