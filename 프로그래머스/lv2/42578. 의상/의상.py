def solution(clothes):
    numCase = 1
    d = {c[-1]:0 for c in clothes}
    for c in clothes:
        d[c[-1]] += 1
    for i in d.values():
        numCase *= i+1 # 공식?으로 받아들임
    return numCase - 1