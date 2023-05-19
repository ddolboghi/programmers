def solution(n, m, section):
    section_set = set(section)
    answer = 0
    i = 1

    while i <= n:
        if i in section_set:
            i += m
            answer += 1
        else:
            i += 1

    return answer
