def solution(progresses, speeds):
    answer = []
    days = []
    # 남은 작업일수 계산
    for p, s in zip(progresses, speeds):
        day = (100-p)//s
        if (100-p)%s != 0:
            day += 1
        days.append(day)
    # print(days)
    i = 0
    while i < len(days):
        cnt = 1
        for j in range(i+1, len(days)):
            if days[i] < days[j]:
                break
            else:
                cnt += 1
        answer.append(cnt)
        i += cnt
    return answer