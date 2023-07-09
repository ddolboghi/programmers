def solution(citations):
    # citations = [1,1,1,1]
    maxCitation = max(citations)
    if maxCitation == 0:
        return 0
    for i in range(0, maxCitation+1):
        h = 0
        for c in citations:
            if c >= i:
                h += 1
        if i > h:
            i = i-1
            break
        elif i == h:
            break
    return i