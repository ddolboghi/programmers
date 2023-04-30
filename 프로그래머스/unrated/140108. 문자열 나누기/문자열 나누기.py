def solution(s):
    answer = 0
    n, i = 1, 1
    while len(s) > 1:
        if s[0] == s[i]:
            n += 1
        else:
            n -= 1
        i += 1
        if n == 0 or len(s[i:]) == 0:
            s = s[i:]
            n, i = 1, 1
            answer += 1
    if len(s) != 0:
        answer += 1
    return answer