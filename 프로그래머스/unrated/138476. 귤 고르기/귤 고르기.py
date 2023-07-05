def solution(k, tangerine):
    answer = 0
    d = dict({i:0 for i in set(tangerine)})
    for i in tangerine:
        d[i] += 1
    arr = sorted([i for i in d.values()], reverse=True)
    for i in arr:
        k -= i
        answer += 1
        if k <= 0:
            break
        
    
    return answer