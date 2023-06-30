from collections import defaultdict
def solution(arr):
    answer = 1
    od = defaultdict(list)
    for a in arr:
        for i, v in decomposition(a).items():
            od[i].append(v)
    for i, v in od.items():
        answer *= i**max(v)
    return answer

def decomposition(n):
    # n을 소인수분해하는 함수
    i = 2
    d = {}
    cnt = 0
    while n > 1:
        if n % i == 0:
            n //= i
            cnt += 1
            d[i] = cnt
        else:
            i += 1
            cnt = 0
    return d