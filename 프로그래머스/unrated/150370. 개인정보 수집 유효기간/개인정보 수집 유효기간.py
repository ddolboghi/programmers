def solution(today, terms, privacies):
    answer = []
    # 테스트 14 틀림
    td = dict({t.split()[0]:int(t.split()[1]) for t in terms})
    tot_d = int(today[:4])*12*28 + int(today[5:7])*28 + int(today[8:])

    for i, p in enumerate(privacies):
        month, year, day = int(p[5:7]), int(p[:4]), int(p[8:10])
        m = (month+td[p[-1]])%12 if (month+td[p[-1]])%12 !=0 else 12
        add_y = (month+td[p[-1]])//12 if (month+td[p[-1]]) % 12 != 0 else (month+td[p[-1]])//12 - 1
        y = year + add_y
        d = day-1
        if d == 0:
            d = 28
            m = m - 1
        if m == 0:
            m = 12
            y = y-1
        print(y,m,d)
        tot_p = y*12*28 + m*28 + d
        if tot_p < tot_d:
            answer.append(i+1)
    return answer
