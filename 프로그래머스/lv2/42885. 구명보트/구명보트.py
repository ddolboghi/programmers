def solution(people, limit):
    answer = 0
    sp = sorted(people)
    s = 0
    e = len(sp)-1
    while s <= e:
        if (sp[s] + sp[e]) > limit:
            answer += 1
            e -= 1
        else:
            answer += 1
            s += 1
            e -= 1
    return answer