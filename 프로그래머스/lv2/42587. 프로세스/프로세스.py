def solution(priorities, location):
    q = []
    i = 0
    idxs = [i for i in range(len(priorities))]
    while priorities:
        if i == len(priorities):
            i = 0
        # i번째 원소가 최대값보다 크거나 같다면
        # priorities에서 제거하고 원소가 1개 줄어드니까 i-1해야 다음 원소로 갈수 있음
        if priorities[i] >= max(priorities):
            q.append(idxs[i])
            priorities.pop(i)
            idxs.pop(i)
            i -= 1
        i += 1
    # print(q)    
    return q.index(location) + 1