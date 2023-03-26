def solution(k, score):
    return [sorted(score[:i])[0] if i<=k else sorted(score[:i], reverse=True)[:k][-1] for i in range(1, len(score)+1) ]