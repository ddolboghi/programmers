def solution(s):
    answer = (len([x for x in s if x in '0123456789'])==len(s)) & (len(s) in [4,6])
    return answer