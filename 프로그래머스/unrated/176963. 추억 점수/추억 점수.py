def solution(name, yearning, photo):
    answer = []
    d = dict(zip(name, yearning))
    print(d)
    for onep in photo:
        inp = set(name) & set(onep)
        temp = 0
        for i in inp:
            temp += d[i]
        answer.append(temp)
    return answer